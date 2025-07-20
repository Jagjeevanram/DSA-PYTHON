class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        all_perm=itertools.permutations(nums)
        unique_perm=set(all_perm)
        li=[]
        for i in unique_perm:
            li.append(list(i))
        return li    
