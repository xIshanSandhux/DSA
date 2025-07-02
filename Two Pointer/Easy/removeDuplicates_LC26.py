from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0

        for x in range(len(nums)):
            if nums[curr]!=nums[x]:
                curr+=1
                nums[curr] = nums[x]

        curr+=1
        return curr
s = Solution()
print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))