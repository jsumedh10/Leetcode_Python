# 3285. Find Indices of Stable Mountains
# Run time - 41ms
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans_list = []
        for i in range(1, len(height)):
            if height[i-1] > threshold:
                ans_list.append(i)
        return ans_list
