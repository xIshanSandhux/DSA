from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstPointer = 0
        lastPointer = len(numbers)-1
        sumList = []
        # print(numbers[firstPointer])
        # print(numbers[lastPointer])

        while firstPointer<lastPointer:
            sum = numbers[lastPointer]+numbers[firstPointer]
            if sum>target:
                lastPointer-=1
            elif sum<target:
                firstPointer+=1
            elif (numbers[lastPointer]+numbers[firstPointer])==target:
                sumList.append(firstPointer+1)
                sumList.append(lastPointer+1)
                return sumList
    
s = Solution()
print(s.twoSum([2,7,11,15],9))
print(s.twoSum([2,3,4],6))
print(s.twoSum([-1,0],-1))