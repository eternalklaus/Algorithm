class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 0,0 0,1 0,2 ... 1,n 2,n
        i, j = 0, 0
        COL, ROW = len(matrix), len(matrix[0])
        checked = [[False for j in range(ROW)] for i in range(COL)]
        
        output = [matrix[0][0]]
        checked[0][0] = True 
        
        def move(direction):
            result = False 
            nonlocal output, i, j
            if direction == 'right':
                i, j = i, j+1 
                while j < ROW and not checked[i][j]:
                    output.append(matrix[i][j])
                    checked[i][j] = True 
                    j += 1
                    result = True 
                j -= 1
            elif direction == 'left':
                i, j = i, j-1 
                while j >= 0 and not checked[i][j]:
                    output.append(matrix[i][j])
                    checked[i][j] = True 
                    j -= 1
                    result = True 
                j += 1
            elif direction == 'down':
                i, j = i+1, j
                while i < COL and not checked[i][j]:
                    output.append(matrix[i][j])
                    checked[i][j] = True 
                    i += 1
                    result = True 
                i -= 1
            elif direction == 'up':
                i, j = i-1, j
                while i < COL and not checked[i][j]:
                    output.append(matrix[i][j])
                    checked[i][j] = True 
                    i -= 1
                    result = True 
                i += 1
            return result 
            
        result = True
        while result:
            ### remember that the place i'm in is already checked^^;
            result = (move('right') & move('down') & move('left') & move('up'))
        return output 