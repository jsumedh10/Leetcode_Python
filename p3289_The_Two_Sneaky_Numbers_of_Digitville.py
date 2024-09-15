'''
3289. The Two Sneaky Numbers of Digitville
Run time - 52ms
'''
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count_dict = {}
        op_list = []
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] == 2:
                op_list.append(num)
        
        return op_list
