class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        count1=0
        count2=0
        ans=0
        for r in range(len(answerKey)):
            if(answerKey[r]=="F"):
                count1+=1
            else:
                count2+=1
            while min(count1,count2)>k:
                if(answerKey[l]=="F"):
                    count1-=1
                else:
                    count2-=1
                l+=1    
            ans=max(ans,r-l+1)
        return ans                        
        