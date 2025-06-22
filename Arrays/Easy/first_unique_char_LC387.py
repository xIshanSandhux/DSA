class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        r=""

        for x in s:
            if x not in d:
                d[x]=1
            elif x in d:
                d[x]+=1
        print(d)

        for key, value in d.items():
            if value==1:
                r = key
                print("firt unique char:",r)
                return s.index(r)

        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))
            