class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        windowFreq = [0]* 26
        s1List = [0]*26

        for x in range (len(s1)):
            s1List[ord(s1[x])-ord('a')] += 1
            windowFreq[ord(s2[x])-ord('a')]+=1
        
        if s1List==windowFreq:
            return True
        
        for i in range(len(s1),len(s2)):
            windowFreq[ord(s2[i])-ord('a')]+=1
            windowFreq[ord(s2[i-len(s1)])-ord('a')]-=1

            if windowFreq==s1List:
                return True
            
        return False
    
s = Solution()

print(s.checkInclusion("ab","eidbaooo"))
print(s.checkInclusion("ab","eidboaooo"))