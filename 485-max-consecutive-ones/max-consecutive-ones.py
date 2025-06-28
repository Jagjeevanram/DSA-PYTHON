class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==1:
                result+=1
                maxi=max(maxi,result)
            else:
                result=0
        return maxi        
               
