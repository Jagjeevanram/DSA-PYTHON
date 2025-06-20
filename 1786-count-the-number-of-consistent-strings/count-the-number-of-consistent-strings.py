class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            if all(i in allowed for i in words[i]):
                count+=1
        return count        