class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        I, J = len(heights), len(heights[0])
        Pacific, Atlantic = set(), set()
        
        def search(i, j, sea):
            
            for newi, newj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not 0<=newi<I or not 0<=newj<J: continue 
                if (newi, newj) in sea: continue 
                
                if heights[newi][newj] >= heights[i][j]: 
                    sea.add((newi, newj))
                    search(newi, newj, sea)
                            
        # top
        i = 0
        for j in range(J):
            Pacific.add((i, j))
            search(i, j, Pacific)
        
        # left 
        j = 0
        for i in range(I):
            Pacific.add((i, j))
            search(i, j, Pacific)
        
        # bottom
        i = I-1
        for j in range(J):
            Atlantic.add((i, j))
            search(i, j, Atlantic)
            
        # right 
        j = J-1
        for i in range(I):
            Atlantic.add((i, j))
            search(i, j, Atlantic)
        
        return [coord for coord in Atlantic if coord in Pacific]