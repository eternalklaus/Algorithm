class Solution:
    def intToRoman(self, num: int) -> str:
        v1    = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        v10   = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C']
        v100  = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M']
        output = ''
        n1000, num = divmod(num, 1000)
        output += 'M' * n1000 
        
        n100, num = divmod(num, 100)
        output += v100[n100]

        n10, num = divmod(num, 10)
        output += v10[n10]

        output += v1[num]

        return output 
