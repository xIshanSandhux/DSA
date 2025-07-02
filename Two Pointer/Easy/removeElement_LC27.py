from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0  

        for x in range(len(nums)):  
            if nums[x] != val:
                nums[curr] = nums[x]
                curr += 1

        return curr 
    
s = Solution()

print(s.removeElement([0,1,2,2,3,0,4,2],2))
print(s.removeElement([3,2,2,3],3))