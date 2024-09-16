# 169. Majority Element
# Run time - 169ms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in set(nums):
            if nums.count(num) > len(nums)/2:
                return num
