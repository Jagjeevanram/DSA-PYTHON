class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        li=[]
        li1=[]
        equal=[]
        left=0
        right=len(nums)-1
        while left<=right:
            if nums[left]<pivot:
                li.append(nums[left])
            elif nums[left]>pivot:
                li1.append(nums[left])
            elif nums[left]==pivot:
                equal.append(nums[left])
            left+=1    
        return li+equal+li1               
        