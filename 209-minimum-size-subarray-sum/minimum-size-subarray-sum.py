class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        ans=float("inf")
        temp=0
        for r in range(len(nums)):
            temp+=nums[r]

            while temp>=target:
                ans=min(ans,r-l+1)
                temp-=nums[l]
                l+=1
        if ans == float("inf"):
            return 0
        return ans    