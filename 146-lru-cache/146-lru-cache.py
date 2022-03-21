class LRUCache:

    def __init__(self, capacity: int):
        self.lrucache = {}
        self.capacity = capacity 

    def get(self, key: int) -> int:
        if key not in self.lrucache: 
            return -1 
        
        # move_to_end
        value = self.lrucache[key]
        del self.lrucache[key]
        self.lrucache[key] = value 
        return value 

    def put(self, key: int, value: int) -> None:
        if key in self.lrucache: # duplicated key -> delete key
            del self.lrucache[key]  
        elif len(self.lrucache) == self.capacity: # delete LRU key
            lrukey = next(iter(self.lrucache.items()))[0]
            del self.lrucache[lrukey]
        self.lrucache[key] = value
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)