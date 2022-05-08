# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def matchrate(word1, word2):
            output = 0
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    output += 1
            return output 
                
        def filterwordlist(word, mn):
            output = []
            for word2 in wordlist:
                if matchrate(word, word2) == mn:
                    output.append(word2)
            return output 
        
        def mostpopuler(wordlist):
            popularities = Counter()
            for word in wordlist:
                for c in word:
                    popularities[c] += 1
            # print (popularities)
            maxpop, output = 0, ''
            for word in wordlist:
                # calculate popularity
                popularity = 0
                for c in word:
                    popularity += popularities[c]
                if popularity > maxpop:
                    maxpop = popularity
                    output = word
            return output 
            
        n = 1
        while True:
            # word = wordlist.pop() ### wordlist중에서 가장 흔한 캐릭터들로 구성된 스트링? 
            word = mostpopuler(wordlist)
            
            mn = master.guess(word) # matched number 
            if mn == 6:
                return word
            wordlist = filterwordlist(word, mn) # find word that (6-mn) diff with word 
