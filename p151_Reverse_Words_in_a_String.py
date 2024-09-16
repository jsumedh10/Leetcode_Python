# 151. Reverse Words in a String
# Run time - 37ms
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
