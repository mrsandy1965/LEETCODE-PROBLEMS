class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=dict()
        for i,n in enumerate(nums):
            temp=target-n
            if temp in a:                                     
                return [a[temp],i]
            a[n]=i