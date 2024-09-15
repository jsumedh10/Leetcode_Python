# 238. Product of Array Except Self

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
