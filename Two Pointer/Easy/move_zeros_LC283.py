from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        isZero = 0
        # isZero=0
        # if len(nums)==1 and nums[0]!=0:
        #     return

        for i,x in enumerate(nums):
            if x!=0:
                temp = nums[isZero]
                nums[isZero] = nums[i]
                nums[i] = temp
                isZero+=1
        print(nums)

        # while nonZero<len(nums):
        #     if nums[isZero]!=0:
        #         isZero+=1
        #         if nums[isZero]==0:
        #             temp = nums[isZero]
        #             nums[isZero] = nums[nonZero]
        #             nums[nonZero] = temp
        #     nonZero+=1

s = Solution()
s.moveZeroes([0,1,0,3,12])
print("-----------")
s.moveZeroes([1,0])