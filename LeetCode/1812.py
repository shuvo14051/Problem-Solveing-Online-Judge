class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        black = "aceg"
        white = "bdfh"
        character = coordinates[0]
        digit = int(coordinates[1])
        if character in black and digit % 2 != 0:
            return False
        elif character in white and digit % 2 == 0:
            return False
        return True
