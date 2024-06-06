class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        from scipy.optimize import linear_sum_assignment
        n = len(nums1)
        cost = [[0 for _ in range(n)] for _ in range(n)]
        # 모든 permutation에서의 cost을 전부 구한다 => i*j가짓수
        for i in range(n):
            for j in range(n):
                cost[i][j] = nums1[i] ^ nums2[j]
        
        row_idx, col_idx = linear_sum_assignment(cost)
        output = 0
        for i, j in zip(row_idx, col_idx):
            output += cost[i][j]
        return output
        