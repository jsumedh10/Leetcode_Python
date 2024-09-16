# 58. Length of Last Word
# Run time - 37ms
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
