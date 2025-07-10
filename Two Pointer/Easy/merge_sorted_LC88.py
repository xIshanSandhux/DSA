from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m-1
        pointer2 = n-1
        mainPointer = m+n-1

        while (pointer2>=0):
            if nums2[pointer2]>=nums1[pointer1]:
                nums1[mainPointer] = nums2[pointer2]
                pointer2-=1
            else:
                nums1[mainPointer] = nums1[pointer1]
                pointer1-=1
            mainPointer-=1



s = Solution()

s.merge([1,2,3,0,0,0],3,[2,5,6],3)
s.merge([1],1,[],0)
s.merge([0],0,[1],1)
        