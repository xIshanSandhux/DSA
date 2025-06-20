from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        print(dic)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))  
            print("Sorted word: ",sorted_word)
            print("sorted(word): ",sorted(word))
            dic[sorted_word].append(word)        
            
        return list(dic.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))