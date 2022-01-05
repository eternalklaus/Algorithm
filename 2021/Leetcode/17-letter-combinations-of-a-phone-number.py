class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # get subset
        alphabet = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        combinations = []
        
        def getsubset(line, leftdigits):
            if leftdigits == '' and line == '': # filtering exceptional input
                return 

            if leftdigits == '':
                combinations.append(line)
                return 

            d = leftdigits[0]
            for apb in alphabet[d]:
                line = line + apb # push
                getsubset(line, leftdigits[1:])
                line = line[:-1] # pop

        getsubset('', digits)
        return combinations
            