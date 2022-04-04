class MyHashMap:

    def __init__(self):
        self.mapsize = 10000
        self.hashmap = [[] for _ in range(self.mapsize)]
        
    def put(self, key: int, value: int) -> None:
        hashkey = key * 31337 % self.mapsize 
        vallist = self.hashmap[hashkey]
        for i, (k, v) in enumerate(vallist):
            if k == key:
                vallist[i] = (key, value)
                return 
        vallist.append((key, value))

    def get(self, key: int) -> int:
        hashkey = key * 31337 % self.mapsize 
        vallist = self.hashmap[hashkey]
        for i, (k, v) in enumerate(vallist):
            if k == key:
                return v 
        return -1 

    def remove(self, key: int) -> None:
        hashkey = key * 31337 % self.mapsize 
        vallist = self.hashmap[hashkey]
        for i, (k, v) in enumerate(vallist):
            if k == key:
                del vallist[i]
                return 
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)