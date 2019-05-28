class Chronos:

    def __init__(self):
        self.head = None
        self.tail = None
        self.map = {}

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
        else:
            return None

    def get(self, key):
        node = self._get_node(key)

        if node:
            return node.data
        else:
            return None

    def set(self, key, data):
        node = self._get_node(key)

        if node:
            node.data = data
        else:
            node = Node(data)
            self._append(node)
            self.map[key] = node


class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
