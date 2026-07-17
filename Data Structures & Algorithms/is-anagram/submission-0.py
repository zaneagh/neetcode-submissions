class Solution:

    def getIntValue(self, char: str) -> int:
        return ord(char) - ord('a')
    
    def isAnagram(self, s: str, t: str) -> bool:
        array = [0] * 26

        if(len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            array[self.getIntValue(s[i])] += 1
            array[self.getIntValue(t[i])] -= 1
        
        for num in array:
            if num != 0:
                return False
        return True;
    


        
        