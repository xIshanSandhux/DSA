from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap ={}
        
        for x in magazine:
            if x not in magazineMap:
                magazineMap[x] = 1
            elif x in magazineMap:
                magazineMap[x]+=1
        print(magazineMap)

        for x in ransomNote:
            if x not in magazineMap:
                return False
            elif x in magazineMap:
                magazineMap[x]-=1
                if magazineMap[x]==0:
                    del magazineMap[x]
        print(magazineMap)
        
        return True
    
s = Solution()
print(s.canConstruct("a","b"))
print(s.canConstruct("aa","ab"))
print(s.canConstruct("aa","aab"))