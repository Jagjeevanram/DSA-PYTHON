class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        li1=[]
        li2=[]
        for i in nums:
            if i%2==0:
                li1.append(i)
            else:
                li2.append(i)
        return li1+li2            