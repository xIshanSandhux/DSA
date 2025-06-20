from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        counter=0

        for x in words:
            for t in x:
                print("Word: ",x)
                if t not in allowedSet:
                    # counter-=1
                    break
            else:
                counter+=1
        return counter
    
s = Solution()
print(s.countConsistentStrings("ab",["ad","bd","aaab","baa","badab"]))