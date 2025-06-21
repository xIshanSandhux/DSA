from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}

        for x in nums:
            if x not in numFreq:
                numFreq[x] = 1
            elif x in numFreq:
                numFreq[x]+=1
        # print(numFreq)
        sorted_numFreq = dict(sorted(numFreq.items(),key=lambda item:item[1],reverse=True))


        arrr=[]
        for key, value in sorted_numFreq.items():
            if len(arrr)<k:
                arrr.append(key)


        return arrr
    

s = Solution()
print(s.topKFrequent([1,1,2,2,2,3,3,3,3,3,3],2))