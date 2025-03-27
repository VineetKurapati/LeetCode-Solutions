class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.stack = []
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.stack.remove(key)
        self.stack.append(key)
        return self.cache[key]
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.stack.remove(key)
        elif len(self.cache) >= self.capacity:
            lru = self.stack.pop(0)
            del self.cache[lru]
        self.cache[key] = value
        self.stack.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)