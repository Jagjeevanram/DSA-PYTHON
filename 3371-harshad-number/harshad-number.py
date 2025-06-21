class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total=0
        temp=x
        while x:
            digit=x%10
            total+=digit
            x=x//10
        return total if temp%total==0 else -1    
            