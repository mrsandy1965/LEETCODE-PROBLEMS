from bisect import bisect_right
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num) 
        result = []
        for q in queries:
            max_length = bisect_right(prefix_sums, q) - 1
            result.append(max_length)                                      
        return result
        