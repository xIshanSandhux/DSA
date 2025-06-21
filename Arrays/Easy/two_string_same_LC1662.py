from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        combined_word_1=""
        combined_word_2 = ""

        for x in word1:
            combined_word_1 = combined_word_1 + x
        
        for x in word2:
            combined_word_2 = combined_word_2 + x
        
        if combined_word_1!=combined_word_2:
            return False
        
        print("Combined word of list word1: ",combined_word_1)
        print("Combined word of list word1: ",combined_word_2)
        return True

s = Solution()
print(s.arrayStringsAreEqual(["a", "cb"],["ab","c"]))
print(s.arrayStringsAreEqual(["ab", "c"],["a","bc"]))