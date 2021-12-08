# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # sum of the depth and weight should be :"MaxDepth+1"
        # lets leverage it calculating the output
        
        # we only need to calculate depth of each component
        depthlist = []
        
        def getdepth(nested, depth):
            for nested_nested in nested:
                l = nested_nested.getList()
                v = nested_nested.getInteger()
                if v == None: v = 0
                    
                if l: 
                    getdepth(l, depth+1)
                else:
                    depthlist.append([depth, v])
        
        # call getdepth reculsively #SOOOOO Dirty data structure
        getdepth(nestedList, 1)
        # print (depthlist)
        
        output = 0
        # calculate the output 
        if depthlist:
            depthlist.sort(reverse=True)
            maxdepth = depthlist[0][0]
            for [d, v] in depthlist:
                output += (maxdepth - d + 1) * v
        return output
        
        
        
        
        
        
        