class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7
        even=(n+1)//2
        odd=n//2
        result=(pow(5,even,mod)*pow(4,odd,mod))%mod
        return result