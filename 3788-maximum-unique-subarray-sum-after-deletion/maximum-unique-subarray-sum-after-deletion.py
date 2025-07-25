class Solution:
    def maxSum(self, nums: List[int]) -> int:
        count=0
        for i in set(nums):
            if i>0:
                count+=i
        if count==0:
            return max(nums)
        return count            