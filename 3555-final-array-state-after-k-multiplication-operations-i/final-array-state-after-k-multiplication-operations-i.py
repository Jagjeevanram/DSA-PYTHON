class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mini=min(nums)
            index=nums.index(mini)
            nums[index]=mini*multiplier
        return nums    