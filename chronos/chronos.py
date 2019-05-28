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
