class LFUCache:

    def __init__(self, capacity: int):
        # build minheap that has values (count, value)
        self.capacity = capacity 
        self.session = 0
        self.total = 0
        self.minheap = [] # (count, session, key)       # sort from min count, sort from min session. 
        self.hashmap = {} # key: (count, session, value)

    def get(self, key: int) -> int:
        self.session += 1
        
        if key in self.hashmap: # key's count += 1 and session update
            (count, session, value) = self.hashmap[key]
            self.hashmap[key] = (count+1, self.session, value)
            return value

        return -1

    def put(self, key: int, value: int) -> None:
        self.session += 1

        if self.capacity == 0: ### boundary case!!!
            return 

        if key in self.hashmap: 
            (old_count, old_session, old_value) = self.hashmap[key]
            self.hashmap[key] = (old_count+1, self.session, value)
            return 

        if self.total == self.capacity: 
            # remove the most least used one 
            while True:
                (heap_count, heap_session, heap_key) = heapq.heappop(self.minheap)
                # print (f'heappop {(heap_count, heap_session, heap_key)}')
                (hash_count, hash_session, hash_value) = self.hashmap[heap_key] # newer value 
                if heap_count == hash_count and heap_session == hash_session: # if heap value is synchronized with hash value,
                    del self.hashmap[heap_key]
                    break 
                heapq.heappush(self.minheap, (hash_count, hash_session, heap_key))
                # print (f'heapush {(self.minheap, (hash_count, hash_session, heap_key))}')
            self.total -= 1
            
        # put value and # key's access count + 1 
        heapq.heappush(self.minheap, (1, self.session, key))
        self.hashmap[key] = (1, self.session, value)
        self.total += 1
        