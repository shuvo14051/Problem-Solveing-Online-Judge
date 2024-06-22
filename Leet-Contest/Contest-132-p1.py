class Solution:
    def clearDigits(s):
        s = list(s)  # Convert string to list for easier manipulation
        while any(c.isdigit() for c in s):  # Continue until no digits are left
            for i in range(len(s)):
                if s[i].isdigit():
                    for j in range(i-1, -1, -1):
                        if not s[j].isdigit():
                            s.pop(i)  # Remove the digit
                            s.pop(j)  # Remove the non-digit character
                            break
                    break  # Restart the loop since we've modified the list
        return ''.join(s)