class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        s1, s2 = 0, 0
        if low < 10:
            low = 10
        for i in range(low, high+1):
            string = str(i)
            if len(string) %2 == 0:
                half = len(string) // 2
                first_half = string[:half]
                second_half = string[half:]
                sum_first_half = sum(int(digit) for digit in first_half)
                # Summing digits in the second half
                sum_second_half = sum(int(digit) for digit in second_half)
                # Comparing the sums
                if sum_first_half == sum_second_half:
                    count += 1
                
        return count
        
s = Solution()
print(s.countSymmetricIntegers(low = 1, high = 100))