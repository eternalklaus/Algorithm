class Bucket:
    def __init__(self):
        self.bucket = []
    def store(self, key, val):
        for idx, [k, v] in enumerate(self.bucket):
            if k == key:
                self.bucket[idx] = [key, val]
                # print ('saving1 .. %d' % key)
                return
        # print ('saving2 .. %d' % key)
        self.bucket.append([key,val])
        
    def delete(self, key):
        for idx, [k, _] in enumerate(self.bucket): 
            if k == key: 
                # print ('deleting .. %d' % key)
                del self.bucket[idx] ### <- remove list component
                return
            
    def read(self, key):
        # print (self.bucket, key)
        for [k, v] in self.bucket:
            if k==key: return v
        return -1
            
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2048
        self.bucket = [Bucket() for i in range(2048)] ###

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.key_space 
        self.bucket[hash_key].store(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_space
        return self.bucket[hash_key].read(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.key_space 
        self.bucket[hash_key].delete(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)