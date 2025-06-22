class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        li=['']*len(s)
        for i in range(len(s)):
            li[indices[i]]=s[i]
        return ''.join(li)   