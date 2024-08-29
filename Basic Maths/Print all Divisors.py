# Given a positive integer N., The task is to find the value of Σi from 1 to N F(i) 
# where function F(i) for the number i is defined as the sum of all divisors of i.

class Solution:
    def sumOfDivisors(self, N: int) -> int:
        total_sum = 0
        
        # Iterate over each number from 1 to N
        for i in range(1, N + 1):
            # Each i contributes i to every multiple of i (i, 2i, 3i, ..., N)
            # The number of multiples of i in [1, N] is N // i
            total_sum += i * (N // i)
        
        return total_sum

# Example usage:
sol = Solution()
print(sol.sumOfDivisors(4))  # Output: 27 (1 + 3 + 7 + 6 + 5 + 5)