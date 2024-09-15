# 3285. Find Indices of Stable Mountains
# Run time - 41ms
'''
Example-
Input: height = [1,2,3,4,5], threshold = 2
Output: [3,4]

Input: height = [10,1,10,1,10], threshold = 3
Output: [1,3]
'''
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans_list = []
        for i in range(1, len(height)):
            if height[i-1] > threshold:
                ans_list.append(i)
        return ans_list
