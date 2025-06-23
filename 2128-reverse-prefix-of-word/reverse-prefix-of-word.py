class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left=0
        right=len(word)-1
        target=-1
        while left<=right:
            if word[left]==ch:
                target=left
                break
            left+=1
        if target!=-1:
            rev=word[:target+1][::-1]
            rem=word[target+1:]

            res=rev+rem
        else:
            res=word  
        return res        
