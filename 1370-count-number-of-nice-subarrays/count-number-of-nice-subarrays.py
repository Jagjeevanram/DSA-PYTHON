class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(nums,k):
            l=0
            ans=0
            temp=0
            for r in range(len(nums)):
                if nums[r]%2==1:
                    temp+=1
                while temp> k:
                    if nums[l]%2==1:
                        temp-=1
                    l+=1
                ans+=r-l+1
            return ans
        a=atMost(nums,k)
        b=atMost(nums,k-1) 
        ans=a-b 
        return ans     
        