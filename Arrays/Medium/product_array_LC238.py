from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        answer=[]
        b = False

        if 0 in nums:
            b = True
            print (nums.index(0))

        for x in nums:
            
            if x!=0:
                product = product*x
        
        for x in nums:
            # print(answer)
            if x <0:
                print(x)
                answer.append(int(product/(x)))
                print(answer)
            elif x==0:
                answer.append(product)
            else:
                answer.append(int(product/x))

        print(product)
        return answer
    
s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))