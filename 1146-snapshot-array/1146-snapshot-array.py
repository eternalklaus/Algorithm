class SnapshotArray:

    def __init__(self, length: int):
        import bisect
        self.next_snap_id = 0
        self.array = [[[-1, 0]] for _ in range(length)] 

    def set(self, index: int, val: int) -> None:
        history = self.array[index]
        if history[-1][0] == self.next_snap_id: # snapshot hasn't shot since previous update 
            history[-1][1] = val # update data
        else:
            history.append([self.next_snap_id, val]) # append current snapshot info  and data

    def snap(self) -> int:
        self.next_snap_id += 1
        return self.next_snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        # print (history, snap_id)
        idx = bisect.bisect(history, [snap_id, 10**9+1]) # if exist, return idx+1. if not exist, return existclose + 1
        return history[idx-1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)