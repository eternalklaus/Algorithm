class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 이전것들중 length 2짜리를 모아오나? 
        # length 2짜리인것들 중에서 나보다 num이 작은것들만 모아오는거지. 크흠. 이계산이 들어가는구나. 
        L = len(nums)
        finals = defaultdict(Counter) # idx: [3:100, 4:150]
        finals[-1] = {-10**6-1:1}
        lis = []

        ### 3번째 인덱스의 값은 5,4,3.. 이렇게 줄어들기만 한다. 
        def lessthen(num, final):
            output = 0 
            for val, cnt in final.items(): # 바로왼쪽 인덱스의 num보다 작은숫자 발견? 그숫자에 귀속된 카운터까지 가져온다
                if val < num:
                    output += cnt
            return output
        
        for num in nums:
            idx = bisect.bisect_left(lis, num) ###
            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num
            
            cnt = lessthen(num, finals[idx-1])
            default = finals[idx].get(num) or 0
            finals[idx][num] = default + cnt # final[idx-1]에 모인 파이널값중 num보다 작아서 lis구성이 가능한 값만 카운팅
        # print (finals)
        return (sum(finals[len(lis)-1].values()))
        
        
        # 3을 가져올땐 3에 귀속된 따까리갯수까지 다 가져와야함...