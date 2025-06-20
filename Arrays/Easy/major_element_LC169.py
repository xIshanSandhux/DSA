from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap ={}
        maxVal =0
        maxNum=0

        for x in nums:
            if x not in countMap:
                countMap[x] = 1
            elif x in countMap:
                countMap[x]+=1
        print(countMap)

        for key, val in countMap.items():
            if val>maxVal:
                maxVal=val
                maxNum= key
        
        print("max val: ",maxVal)
        print("max num: ", maxNum)
        print("half:", len(nums)/2)

        if maxVal> (len(nums)/2):
            return maxNum
    

s = Solution()

print(s.majorityElement([2,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))