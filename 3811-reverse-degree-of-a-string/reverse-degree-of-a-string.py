class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        for i in range(len(s)):
            pos=ord(s[i])-ord('a')
            rev=26-pos
            sum+=rev*(i+1)
        return sum    