class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString=""

        for x in s:
            if x.isalnum():
                newString += x.lower()
        
        firstPointer = 0
        lastPointer = len(newString)-1

        while firstPointer<lastPointer:
            if newString[firstPointer]!=newString[lastPointer]:
                return False
            else:
                firstPointer+=1
                lastPointer-=1

        return True
    
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))