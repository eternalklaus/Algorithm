class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        import bisect
        triplet = [-float('inf')]
        for num in nums:
            # print (triplet)
            idx = bisect.bisect(triplet, num) # [1,2,4,6] bisect(3) would be 2 
            if idx != 0 and triplet[idx-1] == num: ### bisect 는 예의바른 API라서 같은숫자 222가 나오면 가장 뒤의 인덱스를 리턴한다..
                continue 
            
            # if num is less then one of the triplet, 
            if idx < len(triplet): 
                triplet[idx] = num
            else:
                triplet.append(num)
            if len(triplet) >= 4: return True 
        
        return False 
        