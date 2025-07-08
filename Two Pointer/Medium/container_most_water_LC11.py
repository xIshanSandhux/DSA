from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        firstPointer=0
        lastPointer=len(height)-1

        while firstPointer<lastPointer:
            minHeight = min(height[firstPointer],height[lastPointer])
            area = (minHeight)*(lastPointer-firstPointer)
            if area>maxArea:
                maxArea = area
            if minHeight==height[firstPointer]:
                firstPointer+=1
            else:
                lastPointer-=1
        return maxArea
    
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))