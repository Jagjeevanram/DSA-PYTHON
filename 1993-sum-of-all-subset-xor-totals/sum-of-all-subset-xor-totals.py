class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            result|=i
        return result <<(len(nums)-1) 