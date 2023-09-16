class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # z-box

        # 이미z에 적혀있는거 boxsize만큼 베껴오되, 현재box기준 touches the box하는거만 다시구함
        # touches the box -> 노이즈가 섞인거기때문에 재활용 할수가없음
        s = needle + '$' + haystack
        z = [0] * len(s)
        z[0] = 0
        i = 1
        def touches_the_box(left, overlapped):
            return left <= overlapped

        def getboxsize(i):
            boxidx = 0
            while i < len(s):
                if s[boxidx] == s[i]:
                    boxidx += 1
                    i += 1
                else:
                    break
            return boxidx

        while i < len(s):
            boxsize = getboxsize(i)
            z[i] = boxsize
            # 베껴오는 과정
            for boxi in range(1, boxsize):
                if touches_the_box(boxsize-boxi, z[i]):
                    z[i+boxi] = getboxsize(i+boxi)
                else:
                    z[i+boxi] = z[boxi]

            if boxsize == 0: # 0이 겹치던 1이 겹치던 최소1칸은 이동
                i += 1
            else:
                i += boxsize
            # print (i)
        
        output = [i-len(needle)-len('$') for i in range(len(s)) if z[i] == len(needle)]
        if output: return output[0]
        return -1
        