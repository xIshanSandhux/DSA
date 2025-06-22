from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = {}
        dic2 = {}
        r = []

        for x in nums1:
            if x not in dic1:
                dic1[x] = 0
            if x in dic1:
                dic1[x] += 1

        # print(dic1)
        for x in nums2:
            if x not in dic2:
                dic2[x] = 0
            if x in dic2:
                dic2[x] += 1
        # print(dic2)

        for key,value in dic1.items():
            if key in dic2:
                while dic2[key]>0 and dic1[key]>0:
                    # if dic2[key]>0 and dic1[key]>0:
                    r.append(key)
                    dic1[key]-=1
                    dic2[key]-=1
                    

        # print(r)
        # print(dic1)
        # print(dic2)

        return r
    
s = Solution()
print(s.intersect([1,2,2,1],[2,2]))
print(s.intersect([4,9,5],[9,4,9,8,4]))