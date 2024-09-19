'''
11. Container With Most Water
Run time - 487ms
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        first = 0
        last = len(height)-1

        while(first<=last):
            val = min(height[first], height[last]) * (last-first)
            if val > max_val:
                max_val = val 
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1

        return max_val
        
