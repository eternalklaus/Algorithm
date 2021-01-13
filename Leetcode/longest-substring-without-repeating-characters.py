
'''
    * Lesson: Don't use DAC(devide and conquer) method when outer value could effect on inner value.
    *     ex) [ABCD]ZBK <- ZBK's B could effect on ABCD. 
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):     
        def calcmaxlen(s):
            maxlen = 0
            i = j = 0
            while i<len(s) and j<len(s):
                if s[j] in s[i:j]: 
                    # update i to the first appearance
                    offset = s[i:j].index(s[j])
                    i = i + offset + 1

                else:
                    maxlen = max(maxlen, (j + 1) -i)
                    j += 1
            
            return maxlen
        
        return calcmaxlen(s)
                




sl = Solution()
print sl.lengthOfLongestSubstring(" ")
# print sl.lengthOfLongestSubstring("abcdacda")
# on the server, it returns 0. IDK why.