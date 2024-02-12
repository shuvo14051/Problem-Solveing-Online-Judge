from typing import List 

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for i in range(len(seats)):
            moves += abs(students[i] - seats[i])

        return moves
    

s = Solution()
print(s.minMovesToSeat(seats = [4,1,5,9], students = [1,3,2,6]))
