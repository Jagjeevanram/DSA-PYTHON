class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
      

        li = []
        sum1 = 0
        for i in range(len(nums)):
            li.append(sum1)
            sum1 += nums[i]
        li1 = []
        sum2 = 0
        for i in range(len(nums)-1, -1, -1):
            li1.append(sum2)
            sum2 += nums[i]
        li1.reverse()
        li2 = []
        for i in range(len(nums)):
            sub = abs(li[i] - li1[i])
            li2.append(sub)
        return li2

                