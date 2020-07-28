import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if (is_prime[i]):
                for multiple_of_i in range(i*i, n, i):
                    is_prime[multiple_of_i] = False
                    
        return sum(is_prime)
