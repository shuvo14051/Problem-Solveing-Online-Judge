from typing import List 

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        li = []
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                li.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                li.append("Fizz")
            elif (i+1) % 5 == 0:
                li.append("Buzz")
            else:
                li.append(str(i+1))

        return li