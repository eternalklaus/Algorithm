class LFUCache:

    def __init__(self, capacity: int):
        self.minheap = [] # (cnt, timestamp, key) 으로 정렬됨 
        self.timestamp = 0
        self.cache = {} # key: (cnt, timestamp, value)
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        self.timestamp += 1
        if key in self.cache:
            c, t, v = self.cache[key]
            self.cache[key] = (c+1, self.timestamp, v)
            heappush(self.minheap, (c+1, self.timestamp, key))
            return self.cache[key][2]
        return -1

    def put(self, key: int, value: int) -> None:
        self.timestamp += 1
        if key in self.cache: # 키를 추가할 필요가 없는 경우
            c, t, v = self.cache[key] 
            self.cache[key] = (c+1, self.timestamp, value)
            heappush(self.minheap, (c+1, self.timestamp, key))
            return

        if len(self.cache) < self.capacity: # 캐시 여유가 있음
            self.cache[key] = (1, self.timestamp, value)
            heappush(self.minheap, (1, self.timestamp, key))
            return

        else: # 캐시 여유가 없음
            while True:
                (c, t, k) = heappop(self.minheap)
                if k not in self.cache: continue
                (realc, realt, v) = self.cache[k]
                if c == realc and t == realt: break 
            del self.cache[k] # 하나 쫒아내고, 
            self.cache[key] = (1, self.timestamp, value)
            heappush(self.minheap, (1, self.timestamp, key))
            return
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)