from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        pCounter = Counter(p)
        pointer1=0
        windowCounter = 0
        windowString = ""
        returnList = []

        for x in range(len(p)):
            windowString +=s[x]
        windowCounter = Counter(windowString)
        if windowCounter==pCounter:
            returnList.append(pointer1)
      

        for x in range(len(p),len(s)):
            leftChar = s[x-len(p)]
            windowCounter[leftChar]-=1
            if windowCounter[leftChar]==0:
                del windowCounter[leftChar]
            windowCounter[s[x]] += 1
            
            if windowCounter==pCounter:
                pointer1=x - (len(p)-1)
                returnList.append(pointer1)

        return returnList
    
s = Solution()
print(s.findAnagrams("abab","ab"))
print(s.findAnagrams("cbaebabacd","abc"))