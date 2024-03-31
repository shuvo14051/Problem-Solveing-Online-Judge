class Solution:
    def isThree(self, n: int) -> bool:
        li = []
        for i in range(1, n+1):
            if n%i==0:
                li.append(i)

        return len(li) == 3
        