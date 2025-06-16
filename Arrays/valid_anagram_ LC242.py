from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1= {}
        t1 = {}

        if len(s)!= len(t):
            return False
        
        for x in s:
            if x not in s1:
                s1[x] = 1
            elif x in s1:
                s1[x]+=1
        
        # print("s: ",s1)

        for x in t:
            if x not in t1:
                t1[x] = 1
            elif x in t1:
                t1[x]+=1
        # print("t: ",t1)

        for key,value in s1.items():
            if key not in t1:
                return False
            if key in t1:
                if value != t1[key]:
                    return False

        return True
    

s = Solution()

print(s.isAnagram("anagram","nagaram"))
print(s.isAnagram("rat","car"))