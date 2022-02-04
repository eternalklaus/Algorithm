class SnapshotArray:
    from collections import defaultdict 
    
    def __init__(self, length: int):
        self.data = defaultdict(int) # [0] * length  
        self.snapshots = []

    def set(self, index: int, val: int) -> None:
        self.data[index] = val 

    def snap(self) -> int: # returns stap_id 
        self.snapshots.append(self.data.copy())###
        return len(self.snapshots)-1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)