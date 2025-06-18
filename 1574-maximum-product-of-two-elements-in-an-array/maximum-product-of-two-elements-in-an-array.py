class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        li=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product=(nums[i]-1)*(nums[j]-1)
                li.append(product)
        return max(li)  