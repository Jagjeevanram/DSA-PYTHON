class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    sub = abs(i - j)
                    total += sub
                    break  
        return total
