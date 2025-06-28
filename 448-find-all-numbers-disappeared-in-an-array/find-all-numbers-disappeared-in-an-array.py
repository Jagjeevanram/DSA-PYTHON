class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set=set(nums)
        li=[]
        for i in range(1,len(nums)+1):
            if i not in num_set:
                li.append(i)
        return li        