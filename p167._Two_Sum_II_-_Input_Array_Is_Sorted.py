'''
167. Two Sum II - Input Array Is Sorted
Run time - 107ms
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        final_list = []
        first_ptr = 0
        last_ptr = len(numbers)-1

        for i in range(len(numbers)):
            addition = numbers[first_ptr] + numbers[last_ptr]
            if addition == target:
                final_list.append(first_ptr+1)
                final_list.append(last_ptr+1)
                break
            if(addition > target):
                last_ptr -= 1
            if(addition < target):
                first_ptr += 1
        return final_list

        
