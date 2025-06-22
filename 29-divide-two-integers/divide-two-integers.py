class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        maxi=2**31-1
        mini=-2**31
        if dividend==mini and divisor==-1:
            return maxi


        return int(dividend/divisor)