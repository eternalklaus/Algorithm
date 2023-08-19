class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        palicases = []

        def ispalin(i, j):
            j -= 1 # adjustment
            while i<j:
                if s[i] != s[j]:
                    return False 
                i += 1
                j -= 1
            return True

        def append_palindrom(lpivot, case): # I want to save cache but i also have to append case..
            nonlocal palicases
            if lpivot == n:
                palicases.append(case.copy())
                return 

            for i in range(lpivot+1, n+1):
                if ispalin(lpivot, i):
                    case.append(s[lpivot:i])
                    append_palindrom(i, case)
                    case.pop()

        append_palindrom(0, [])
        return palicases
