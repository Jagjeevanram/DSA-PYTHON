class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        l = sorted(Counter(word).values())

        @cache
        def f(i, j):
            if i >= j: return 0
            rem = l[j] - l[i] - k
            if rem <= 0: return 0
            return min(l[i] + f(i+1,j), rem + f(i,j-1))
        
        return f(0,len(l)-1)