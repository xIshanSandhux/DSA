from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = 0
        for x in range(k):
            curSum+=nums[x]
        maxAvg = curSum/k

        for x in range(k,len(nums)):
            curSum+=nums[x]
            curSum-=nums[x-k]

            maxAvg = max(maxAvg,(curSum/k))
        return maxAvg