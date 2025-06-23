class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        leftsum=sum(nums)
        digit=0
        for i in range(len(nums)):
            n=nums[i]
            while n>0:
                digit+=n%10
                n=n//10
        return leftsum-digit        
