# 27. Remove Element
# Run Time - 33ms -> only one pass over the list

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[ptr] = nums[i]
                ptr += 1

        return ptr


# Run Time - 39ms -> Using two pointers approach

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         first = 0
#         last = len(nums)-1
#         while(first <= last):
#             if nums[last] == val:
#                 last -= 1
#                 continue
#             if nums[first] == val:
#                 nums[first], nums[last] = nums[last], nums[first]
#                 last -= 1
#             first += 1

#             print(" ".join([str(x) for x in nums]))
            

#         return first

