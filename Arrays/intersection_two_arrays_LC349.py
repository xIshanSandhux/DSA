from typing import List


# As they only want the unique values for the intersection, i am converting both the lists into a hash set, 
# so that i have O(1) look up and then i am just looping through any 1 set and checking if that element is present in the other set
# if it is present i am appending to the list.
# and then i am just returing the list at the end
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(nums1)
        num2 = set(nums2)
        r = []

        for x in num1:
            if x in num2:
                r.append(x)
        return r
    
s = Solution()
print(s.intersection([1,2,2,1],[2,2]))
print(s.intersection([4,9,5],[9,4,9,8,4]))