from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        firstPointer = 0
        lastPointer = len(s)-1
        beforestr = ""
        afterstr = ""


        beforestr = "".join(s)

        while firstPointer<lastPointer:
            temp = s[firstPointer]
            s[firstPointer] = s[lastPointer]
            s[lastPointer] = temp
            firstPointer+=1
            lastPointer-=1

        afterstr = "".join(s)

        print("before string: ", beforestr)
        print("after string: ", afterstr)
        print("----------------------------------")

s = Solution()

s.reverseString(["h","e","l","l","o"])
s.reverseString(["H","a","n","n","a","h"])

        