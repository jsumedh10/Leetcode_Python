# 1342. Number of Steps to Reduce a Number to Zero

# runtime - 32ms
class Solution:
    def numberOfSteps(self, num: int) -> int:
        num_of_steps = 0
        while (num != 0):
            if num%2==0:
                num = num/2
            else:
                num -= 1
            num_of_steps+=1
        return num_of_steps
