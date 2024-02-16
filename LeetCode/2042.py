class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        li = []
        s_li = s.split(' ')
        for i in s_li:
            if i.isdigit():
                li.append(int(i))

        for i in range(1, len(li)):
            if li[i-1] >= li[i]:
                return False
                        
        return True

s = Solution()
print(s.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))