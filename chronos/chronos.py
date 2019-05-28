import asyncio
import json
import socket

import click
import pendulum


class Chronos:
    """Chronos LRU cache library with time expiration"""

    def __init__(self, max_size=100):
        """Initializes Chronos

        Parameters
        ----------
        max_size : int
            Maximum number of pages to be cached
        """
        self.head = None
        self.tail = None
        self.map = {}
        self.max_size = max_size

    def __len__(self):
        return len(self.map)

    def _append(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node

    def _pop(self):
        if self.tail:
            node = self.tail

            if node.prev:
                self.tail = node.prev
            else:
                self.head = None
                self.tail = None

            return node

    def _remove(self, node):
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if not node.prev and node.next:
            self.head = node.next
        elif node.prev and not node.next:
            self.tail = node.prev
        elif not node.prev and not node.next:
            self.head = None
            self.tail = None

        node.next = None
        node.prev = None

    def _get_node(self, key):
        if key in self.map:
            node = self.map[key]
            self._remove(node)

            if not node.ttu or node.ttu >= pendulum.now():
                self._append(node)

                return node

    def get(self, key):
        """Gets the cached content by its key

        Parameters
        ----------
        key : hashable
            Any hashable that represents the key
            of the resource to be retrieved

        Return
        ------
        any
            The content cached
        """
        node = self._get_node(key)

        if node:
            return node.data

    def set(self, key, data, expiration=None):
        """Store content by its key

        Parameters
        ----------
        key : hashable
            Any hashable that represents the key
            of the resource to be cached
        data : any
            The content to be cached
        expiration : int/float
            The expiration in seconds. When setted,
            the cached content will be available
            until its expiration.
        """
        node = self._get_node(key)

        if node:
            node.data = data
        else:
            if len(self) + 1 > self.max_size:
                node = self._pop()
                del self.map[node.key]

            node = Node(key, data, expiration)
            self._append(node)
            self.map[key] = node


class Node:
    """The cached page element"""

    def __init__(self, key, data, expiration=None):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

        if expiration:
            self.ttu = pendulum.now().add(seconds=expiration)
        else:
            self.ttu = None


class ChronosServer:
    """Async server Start the cache"""

    def __init__(self, host='127.0.0.1', port=9191, max_size=100):
        self.host = host
        self.port = port
        self.chronos = Chronos(max_size)
        # create asyncio event loop
        self._loop = asyncio.get_event_loop()
        # create the coroutine that will bind the socket with the port
        coroutine = asyncio.start_server(
            self.request_handler, host, port, loop=self._loop,
            family=socket.AF_INET,
        )
        # run the coroutine to obtain the server socket
        self._socket = self._loop.run_until_complete(coroutine)

    def run(self):
        print(f'Server listening at {self.host}:{self.port}...')

        try:
            self._loop.run_forever()
        except KeyboardInterrupt:
            print('Terminating server...')

        self._socket.close()
        self._loop.run_until_complete(self._socket.wait_closed())
        self._loop.close()

        print('Server closed')

    async def request_handler(self, reader, writer):
        address = writer.get_extra_info('peername')

        print(f'Connection received from {address}')

        data = await reader.readuntil(b'\r\n')

        cmd = json.loads(data.decode().strip())

        if cmd.get('command') == 'set':
            self.chronos.set(
                cmd.get('key'),
                cmd.get('value'),
                cmd.get('expiration'),
            )
        elif cmd.get('command') == 'get':
            writer.write(json.dumps({
                'return': self.chronos.get(cmd.get('key')),
            }).encode())
            await writer.drain()
        else:
            print('Invalid command')

        writer.write(b'\r\n')
        await writer.drain()

        writer.close()


class ChronosClient:
    """Async client to comunicate with the Chronos Server"""

    def __init__(self, host='127.0.0.1', port=9191):
        self.host = host
        self.port = port

    async def send_command(self, command):
        reader, writer = await asyncio.open_connection(self.host, self.port)

        writer.write(f'{command}\r\n'.encode())
        await writer.drain()

        result = await reader.readuntil(b'\r\n')

        writer.close()
        await writer.wait_closed()

        return result

    async def set(self, key, value, expiration=None):
        command = json.dumps({
            'command': 'set',
            'key': key,
            'value': value,
            'expiration': expiration,
        })

        await self.send_command(command)

    async def get(self, key):
        command = json.dumps({
            'command': 'get',
            'key': key,
        })

        result = await self.send_command(command)

        return json.loads(result).get('result')


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if not ctx.invoked_subcommand:
        click.echo(ctx.get_help())


@cli.command('server', help='Starts the Chronos Server')
@click.option('--host', '-h', default='127.0.0.1', help='Server host')
@click.option('--port', '-p', default=9191, help='Server port')
def server(host, port):
    try:
        server = ChronosServer()
    except OSError as error:
        print(f'Failed to create the server:\n{error}')
    else:
        server.run()


if __name__ == '__main__':
    cli()
