class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lrucache = {}
        self.accessed = []
        self.counter = Counter()

    def get(self, key: int) -> int:
        if key in self.lrucache:
            self.accessed.append(key)
            self.counter[key] += 1
            return self.lrucache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.lrucache) == self.capacity:
            if key not in self.lrucache: 
                # evict key
                while True:
                    k = self.accessed.pop(0)
                    self.counter[k] -= 1
                    if self.counter[k] == 0: break 
                del self.lrucache[k]
        
        self.lrucache[key] = value 
        self.accessed.append(key)
        self.counter[key] += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)