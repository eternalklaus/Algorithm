class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 1) one word: left
        # 2) last line : left 
        # 3) else: devide evenly, giving more slots on left 
        
        
        def makeline(currentline, direction=''):
            if len(currentline) == 1: direction = 'LEFT'
            output = ''

            if direction == 'LEFT':
                for word in currentline:
                    output += word
                    output += ' '
                output = output[:len(output)-1] # except for last appending spaces
                output += ' ' * (maxWidth - len(output))
                return output 

            else:
                spaces = maxWidth - len(''.join(currentline))
                space = spaces // (len(currentline) - 1)
                modulo = spaces % (len(currentline) - 1)
                
                for word in currentline:
                    output += word 
                    output += ' ' * space 
                    output += ' ' * (modulo > 0)
                    modulo -= 1
                return output[:len(output)-space] # except the last appending spaces   
            
            
        output = []
        cnt, currentline = 0, []
        
        for word in words: 
            if cnt + len(word) > maxWidth: # overflowed in here 
                output.append(makeline(currentline)) # default = medium, if len(currentline) == 1: left 
                cnt, currentline = 0, []
            
            # add word into currentline 
            currentline.append(word)
            cnt += len(word) + 1

        output.append(makeline(currentline, 'LEFT'))
        return output