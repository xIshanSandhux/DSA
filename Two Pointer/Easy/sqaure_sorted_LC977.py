from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        firstPointer = 0
        lastPointer = len(nums)-1
        position = len(nums)-1
        sortedList = [0]* (len(nums))

        while firstPointer<=lastPointer:
            num1 = nums[firstPointer]**2
            num2 = nums[lastPointer]**2
            print(f"num1: {num1} | num2: {num2}")
            
            if num1>num2:
                sortedList[position] = num1
                firstPointer+=1
            else:
                sortedList[position] = num2
                lastPointer-=1
            print(sortedList[position])
            position-=1
        

        return sortedList
    
s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))