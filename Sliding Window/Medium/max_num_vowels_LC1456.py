class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVow = 0
        curVow =0
        vowelSet = set()
        vowels = "aeiou"

        for x in vowels:
            vowelSet.add(x)

        for x in range(k):
            if s[x] in vowelSet:
                curVow+=1
        maxVow = max(curVow,maxVow)

        for i in range(k,len(s)):
            if s[i] in vowelSet:
                curVow+=1
            if s[i-k] in vowelSet:
                curVow-=1
            maxVow = max(maxVow,curVow)

        return maxVow
    
s = Solution()
print(s.maxVowels("abciiidef",3))
print(s.maxVowels("aeiou",2))
print(s.maxVowels("leetcode",3))