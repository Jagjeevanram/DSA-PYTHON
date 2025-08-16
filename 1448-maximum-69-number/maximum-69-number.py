class Solution:
    def maximum69Number (self, num: int) -> int:
        array=list(str(num))
        for i in range(len(array)):
            if array[i]=='6':
                array[i]='9'
                break
        return int(''.join(array))        
