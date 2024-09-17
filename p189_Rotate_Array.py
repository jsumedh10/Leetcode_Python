# 189. Rotate Array
# Run time - 151ms
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # -1 * 2 + 1 = -1
        # quotient*divisor + remainder = dividend
        x = (len(nums) - k) % len(nums)
        nums[:] = nums[x:] + nums[:x]
        return nums
