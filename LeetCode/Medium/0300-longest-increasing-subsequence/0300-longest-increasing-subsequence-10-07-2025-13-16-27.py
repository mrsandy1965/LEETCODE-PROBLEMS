dp = [[0] * 100 for _ in range(100)]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(n):
            for j in range(n):
                if i > j and nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1 , dp[i])
        return max(dp)
