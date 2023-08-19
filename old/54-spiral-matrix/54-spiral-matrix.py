class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        COL, ROW, VISITED = len(matrix), len(matrix[0]), 101
        
        #// initialize output array 
        output = [matrix[0][0]]
        matrix[0][0] = VISITED # check it's visited
        
        #// moving step. novel!
        gogo = {'right':[0, 1], 'down':[1, 0], 'left':[0, -1], 'up':[-1, 0]}
        
        def move(way):
            nonlocal i, j, output 
            i, j = i + gogo[way][0], j + gogo[way][1]
            result = False
            
            while (0 <= i < COL and 0 <= j < ROW) and matrix[i][j] != VISITED:
                output.append(matrix[i][j])
                matrix[i][j] = VISITED 
                result = True
                i, j = i + gogo[way][0], j + gogo[way][1]
            
            i, j = i - gogo[way][0], j - gogo[way][1]
            return result
                
        
        result = True
        while result:
            result = (move('right') & move('down') & move('left') & move('up'))
        return output 