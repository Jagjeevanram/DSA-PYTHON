class Solution:
    def maxFreqSum(self, s: str) -> int:
        dici={}
        vowels="aeiou"
        for i in s:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        max_vov=0
        max_con=0       
        for key,val in dici.items():
            if key in vowels:
                max_vov=max(max_vov,val)
            else:
                max_con=max(max_con,val)
        return max_vov+max_con            

        