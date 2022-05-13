class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find median value of nums1+nums2 
        total = len(nums1) + len(nums2)
        
        def kth(a, b, k):
            if not a: return b[k]
            if not b: return a[k]

            i1, i2 = len(a)//2, len(b)//2

            if i1 + i2 < k: # 각각 3번째, 4번째 인데 k 는 10번째 인 상황 
                if a[i1] < b[i2]: # a아래를 날려버려
                    return kth(a[i1+1:], b, k-i1-1) ###
                else: #b아래를 날려버려
                    return kth(a, b[i2+1:], k-i2-1)
            
            else: # elif i1 + i2 >= k: # 각각 3번째, 4번째 인데 k는 2번째인 상황 
                if a[i1] < b[i2]: # b위를 날려버려
                    return kth(a, b[:i2], k) # 3,4인데 k=7일 것을 대비 
                else: # a위를 날려버려
                    return kth(a[:i1], b, k)
        
        if total % 2: # 홀수 -> 7개라면 3
            return kth(nums1, nums2, total // 2)
        else: # 짝수 -> 4라면 2, 1
            return (kth(nums1, nums2, total // 2) + kth(nums1, nums2, total // 2 - 1)) / 2
            
                