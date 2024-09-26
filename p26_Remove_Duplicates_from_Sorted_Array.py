'''
26. Remove Duplicates from Sorted Array
Run time - 84ms
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i]
                left += 1
        return left
