class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        li1=[]
        li2=[]
        li=[]
        for i in nums:
            if i%2==0:
                li1.append(i)
            else:
                li2.append(i)
        for j in range(len(nums)):
            if j%2==0:
                li.append(li1[j//2])
            else:
                li.append(li2[j//2])
        return li        

        