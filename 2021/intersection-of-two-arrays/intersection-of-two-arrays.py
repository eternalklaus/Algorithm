class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 59 ms, faster than 30.16% 
        '''
        set1 = set(nums1) 
        set2 = set(nums2) 
        return set1 & set2 
        '''
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        output = []
        while True:
            if i == len(nums1) or j == len(nums2): return output
            number1 = nums1[i]
            number2 = nums2[j]
            print (number1, number2)
            
            if number1 == number2: 
                output.append(number1) 
                while i < len(nums1) and nums1[i] == number1:
                    i += 1
                while j < len(nums2) and nums2[j] == number2:
                    j += 1
            elif number1 < number2:
                while i < len(nums1) and nums1[i] < number2:
                    i += 1
            elif number1 > number2:
                while j < len(nums2) and number1 > nums2[j]:
                    j += 1
            