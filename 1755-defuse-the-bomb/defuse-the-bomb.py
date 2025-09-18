class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        nums1=code+code
        n=len(code)
        if k==0:
            return [0]*n
        elif k>0:
            return [sum(nums1[i+1:i+1+k]) for i in range(n) ]
        else:
            k=abs(k)      
            return [sum(nums1[i+n-k:i+n]) for i in range(n) ]