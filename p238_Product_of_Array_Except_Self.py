# 238. Product of Array Except Self

# Accepted solution - Try 3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)

        prefix_product = 1
        for i in range(len(nums)):
            result[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
        
        return result

# Try 1
'''
import math
class Solution:
  answer = []
  for i in range(len(nums)):
    left = math.prod(nums[:i])
    right = math.prod(nums[i+1:])
    answer.append(left*right)
    return answer
'''

# Try 2
'''
class Solution:
    def mult(self, num_list):
        product = 1
        for num in num_list:
            product *= num
        return product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            answer.append(self.mult(nums[:i]) * self.mult(nums[i+1:]))
        return answer
'''
