
class _Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("limit must be greater than zero")

        self.limit = limit
        self.cache = {}
        self.head = _Node()
        self.tail = _Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _mark_as_used(self, node):
        self._remove(node)
        self._add_to_front(node)

    def get(self, key):
        node = self.cache.get(key)

        if node is None:
            return None

        self._mark_as_used(node)
        return node.value

    def set(self, key, value):
        node = self.cache.get(key)

        if node is not None:
            node.value = value
            self._mark_as_used(node)
            return

        node = _Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.limit:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]