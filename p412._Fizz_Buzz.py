# 412. Fizz Buzz

# time - 52ms
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        final_list = []
        for num in range(1,n+1):
            is_divisible_by_3 = num%3==0
            is_divisible_by_5 = num%5==0

            if(is_divisible_by_3 and is_divisible_by_5):
                final_list.append("FizzBuzz")
                continue
            if(is_divisible_by_3):
                final_list.append("Fizz")
                continue
            if(is_divisible_by_5):
                final_list.append("Buzz")
                continue
            else:
                final_list.append(str(num))
        return final_list
