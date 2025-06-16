from typing import List


# The brute force method is basically just have a nested for loop and then return both the indexes
# for the optimized method:
# Created a dictionary which will store {num:index}
# looping through the list using enumerate because i need the index along with the value
# then I am checking if the diff is in the dic or not, if it is then i am just returning the index of the diff value and the current index
# if its not in the dic then i am just storing the current num as the key and the the index of the num as the value of the key
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index,value in enumerate(nums):
            diff = target - value

            if diff in seen:
                return [seen[diff],index]
            else:
                seen[value] = index
       
    

s = Solution()
print(s.twoSum([2,7,11,15],9))
print(s.twoSum([3,2,4],6))
print(s.twoSum([3,2,3],6))