from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
    
        write = 2 

        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write
    
s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))