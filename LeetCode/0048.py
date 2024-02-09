# class Solution:
#     def rotate(self, matrix) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         matrix = list(map(list, zip(*matrix)))

#         matrix = [i[::-1] for i in matrix]

#         return matrix
        
# s = Solution()
# print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))

class Solution:
    def rotate(self, matrix) -> None:
        matrix[:] = zip(*matrix[::-1])