from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        seen = set()
        for x in range(len(nums)+1):
            if x not in seen:
                seen.add(x)
    
        for x in nums:
            if x in seen:
                seen.remove(x)


        if len(seen)!=0:
            return seen.pop()
        
    
    
s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))