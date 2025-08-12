class Solution(object):
    def scoreOfString(self, s):
        ans=0
        for i in range(len(s)-1):
            a=ord(s[i])
            b=ord(s[i+1])
            temp=abs(b-a)
            ans=ans+temp

        return ans    
    
        
   
   