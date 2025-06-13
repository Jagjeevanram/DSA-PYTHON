class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n=len(nums)
        def can_form_pairs(max_diff):
            count=0
            i=1
            while i<n:
                if nums[i]-nums[i-1]<=max_diff:
                    count+=1
                    i+=2
                else:
                    i+=1
            return count>=p
        left=0
        right=nums[-1]-nums[0]
        result=right
        while left<=right:
            mid=(left+right)//2
            if can_form_pairs(mid):
                result=mid
                right=mid-1
            else:
                left=mid+1
        return result                  
