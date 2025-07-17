class Solution:
    def minElement(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(len(nums)):
            num = nums[i]
            sum1 = 0
            while num:
                digit = num % 10
                sum1 += digit
                num //= 10
            li.append(sum1)
        return min(li)