
from collections import OrderedDict


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("limit must be greater than zero")

        self.limit = limit
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None

        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return

        self.cache[key] = value

        if len(self.cache) > self.limit:
            self.cache.popitem(last=False)
