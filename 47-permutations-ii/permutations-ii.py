class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = set(itertools.permutations(nums)) 
        return [list(i) for i in perm]
