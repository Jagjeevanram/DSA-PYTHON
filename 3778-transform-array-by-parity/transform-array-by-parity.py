class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        li = []
        for num in nums:
            if num % 2 == 0:
                li.append(0)
            else:
                li.append(1)
        li.sort()
        return li
