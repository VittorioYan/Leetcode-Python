from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_dict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lru_dict:
            self.lru_dict.move_to_end(key=key, last=True)
            return self.lru_dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_dict:
            self.lru_dict.move_to_end(key=key, last=True)
        self.lru_dict[key] = value
        if len(self.lru_dict) > self.capacity:
            self.lru_dict.popitem(last=False)


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)

