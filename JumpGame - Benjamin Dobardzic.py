class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)      
        @cache
        def dfs(j):
            if j >= n - 1:
                return True
            for i in range(1, nums[j] + 1):
                if j + i >= n:
                    break
                if dfs(j + i):
                    return True
            return False
        return dfs(0)