class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = Counter()
        self.lrucache = {} # should be less then capacity
        self.accessed = []

    def get(self, key: int) -> int:
        self.accessed.append(key)
        self.counter[key] += 1
        # self.lrucache.get(key) ### 0 인 경우 존재.. 
        # print (self.lrucache, key)
        if key in self.lrucache:
            return self.lrucache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.lrucache) == self.capacity:
            # evict key
            if key not in self.lrucache: # new key would be inserted
                while True:
                    k = self.accessed.pop(0)
                    self.counter[k] -= 1
                    if self.counter[k] == 0 and k in self.lrucache: ### 아무생각 없이 get한 경우 
                        break 
                del self.lrucache[k]
        self.lrucache[key] = value
        self.accessed.append(key)
        self.counter[key] += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)