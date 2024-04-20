class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end to denote it as most recently used
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key already exists, update its value and move it to the end
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # If cache is full, remove the least recently used key (first item)
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value
