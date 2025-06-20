from typing import List

# creating a hash set which will be storing the elements that I am looping through and I am using hash set because its time complexity is O(1) for inserting, and searching
# and then am checking ifthe current element is in the set, if it is then i am just returning true. 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for x in nums:
            # print("values of x: ",x)
            if x not in s:
                s.add(x)
                # print("set: ",s)
            elif x in s:
                return True
        return False
    

s = Solution()

print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))