class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        length = len(s)
        output = ["0"]*length
        one_count = s.count("1")
        output[-1] = "1"
        one_count -= 1
        start_index = 0

        while one_count:
            output[start_index] = "1"
            one_count -= 1
            start_index += 1
        result = "".join(output)
        return result
    
s = Solution()
print(s.maximumOddBinaryNumber("0110"))