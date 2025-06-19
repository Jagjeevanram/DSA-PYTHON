class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and nums[i] not in li:
                    li.append(nums[i])
        return li            