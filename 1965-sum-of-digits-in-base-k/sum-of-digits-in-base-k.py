class Solution:
    def sumBase(self, n: int, k: int) -> int:
        li=[]
        while n:
            div=n%k
            li.append(div)
            n=n//k
        return sum(li)    
