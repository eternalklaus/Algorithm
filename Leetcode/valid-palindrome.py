class Solution(object):

    ### compare with reverse: Runtime: 96 ms
    def isPalindrome(self, s):
        s_filtered          = filter(lambda ch:ch.isalnum(),s)
        s_filtered_lower    = map(lambda ch:ch.lower(),  s_filtered)
        
        s_filtered_lower_reverse = s_filtered_lower[::-1]
        print s_filtered_lower_reverse
        print s_filtered_lower

        return s_filtered_lower == s_filtered_lower_reverse


s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
