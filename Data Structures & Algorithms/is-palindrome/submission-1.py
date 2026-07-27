class Solution:
    def isPalindrome(self, s: str) -> bool:
        santizedString = ''.join(filter(str.isalnum, s)).lower()

        l = 0
        r = len(santizedString) - 1
    
        while l < (len(santizedString) - 1) / 2:
            print("l" + str(l))
            print("r" + str(r))
            if santizedString[l] != santizedString[r]:
                return False
            l += 1
            r -= 1
        return True
        