class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        uniqueChar = set()
        count=0
        maxCount=0
        pointer1=0


        for x in range(len(s)):
            while s[x] in uniqueChar:
                uniqueChar.remove(s[pointer1])
                pointer1+=1
            
            uniqueChar.add(s[x])
            maxCount = max(maxCount,(x-pointer1+1))

        return maxCount
    
s= Solution()

print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("bbbbbbbb"))
