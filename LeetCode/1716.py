class Solution:
    def totalMoney(self, n: int) -> int:
        start = 1
        s = 0
        count = 1
        while count <= n:
            s += start + (count - 1) % 7
            count += 1
            if count % 7 == 1:
                start += 1
        return s

s = Solution()
print(s.totalMoney(20))  # Output: 37



# class Solution:
#     def totalMoney(self, n: int) -> int:
#         start = 1
#         temp = start
#         s = 0
#         count = 0
#         for i in range(n):
#             s+=start
#             start += 1
#             count +=1

#             if count % 3 == 0:
#                 temp+=1
#         return s


