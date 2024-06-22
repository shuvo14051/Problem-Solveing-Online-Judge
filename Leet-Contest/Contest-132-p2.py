from collections import deque
from typing import List

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if k >= n - 1:  # if k is larger than the number of players - 1
            return skills.index(max(skills))  # the player with max skill wins all
        
        queue = deque(range(n))
        consecutive_wins = 0
        current_winner = queue.popleft()
        
        while consecutive_wins < k:
            next_player = queue.popleft()
            if skills[current_winner] > skills[next_player]:
                consecutive_wins += 1
                queue.append(next_player)
            else:
                queue.append(current_winner)
                current_winner = next_player
                consecutive_wins = 1
        
        return current_winner

# Example usage:
solution = Solution()
print(solution.findWinningPlayer([4, 2, 6, 3, 9], 2))  # Output: 2
print(solution.findWinningPlayer([2, 5, 4], 3))  # Output: 1
