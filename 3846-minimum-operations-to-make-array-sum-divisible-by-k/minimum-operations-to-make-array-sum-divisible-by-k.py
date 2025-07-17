class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum1=sum(nums)
        remainder=sum1%k
        return remainder