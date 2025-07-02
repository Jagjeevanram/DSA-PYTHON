class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low=0
        high=len(s)
        result=[]
        for i in s:
            if i=="I":
                result.append(low)
                low+=1
            else:
                result.append(high)
                high-=1
        result.append(low)#if both are qual i,e; low=high
        return result          



       