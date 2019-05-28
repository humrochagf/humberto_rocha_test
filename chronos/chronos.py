class Chronos:

    def __init__(self, max_size=100):
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
            self._append(node)

            return node

    def get(self, key):
        node = self._get_node(key)

        if node:
            return node.data

    def set(self, key, data):
        node = self._get_node(key)

        if node:
            node.data = data
        else:
            if len(self) + 1 > self.max_size:
                node = self._pop()
                del self.map[node.key]

            node = Node(key, data)
            self._append(node)
            self.map[key] = node


class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None
