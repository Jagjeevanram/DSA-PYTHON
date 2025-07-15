class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowel=False
        consonant=False
        for i in word:
            if not i.isalnum():
                return False
            if i.isalpha():
                lower=i.lower()
                if lower in 'aeiou':
                    vowel=True
                else:
                    consonant=True
            if vowel and consonant:
                continue
        return vowel and consonant                         