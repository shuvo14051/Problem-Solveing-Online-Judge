class Solution:

    def prime(self, value):
        count = 0
        if value == 1:
             return False
        for i in range(2, value):
            if value % i == 0:
                count += 1
        if count == 0:
            return True
        else:
            return False
            
        
            
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c = 0
        for num in range(left, right+1):
            binary = bin(num)[2:]
            count_one = binary.count("1")
            prime_or_not = self.prime(count_one)
            if prime_or_not:
                c += 1
        return c
    
s = Solution()
print(s.countPrimeSetBits(6, 10))
