# 1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            nums[i+1] += nums[i]
        return nums
