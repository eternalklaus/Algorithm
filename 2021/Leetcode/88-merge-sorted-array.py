class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        size1, size2 = m, n 
        
        # compare from the front
        '''
        nums1_copy = nums1[:m]
        p1, p2 = 0,0
        for i in range(m + n):
            
            if p2 == size2 or (p1 < size1 and nums1_copy[p1] <= nums2[p2]):
                nums1[i] = nums1_copy[p1]
                p1 += 1
            elif p1 == size1 or (p2 < size2 and nums1_copy[p1] > nums2[p2]):
                nums1[i] = nums2[p2]
                p2 += 1
        '''
        
        # compare from the back
        p1, p2 = size1-1, size2-1
        for i in range(m+n-1, -1, -1):
            if p2 < 0 or (p1 >= 0 and nums1[p1] > nums2[p2]):
                nums1[i] = nums1[p1]
                p1 -= 1
            elif p1 < 0 or (p2 >= 0 and nums1[p1] <= nums2[p2]):
                nums1[i] = nums2[p2]
                p2 -= 1
            