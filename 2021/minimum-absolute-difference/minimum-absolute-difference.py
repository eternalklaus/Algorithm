class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        from collections import defaultdict
        
        arr.sort()
        diff = defaultdict(list)
        mindiff = arr[1]-arr[0]
        
        for i in range(1, len(arr)):
            diff[arr[i]-arr[i-1]].append([arr[i-1], arr[i]])
            mindiff = min(mindiff, arr[i]-arr[i-1])
        
        return diff[mindiff]
        
        
        