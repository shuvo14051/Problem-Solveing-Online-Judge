class Solution:
    def minimumChairs(self, s: str) -> int:
        chair = 0
        max_chairs = 0

        for person in s:
            if person == "E":
                chair += 1
                max_chairs = max(max_chairs, chair)
            elif person == "L":
                chair -= 1

        return max_chairs

solution = Solution()

print(solution.minimumChairs("EEEE"))
