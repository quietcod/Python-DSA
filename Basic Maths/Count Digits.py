# Given a number n. Count the number of digits in n which evenly divide n. 
# Return an integer, total number of digits of n which divides n evenly.
# Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.

# method 1

# def count_divisible_digits(n: int) -> int:
#     count = 0
#     for digit in str(n):
#         if digit != '0':  # Skip if digit is 0
#             if n % int(digit) == 0:
#                 count += 1
#     return count

# # Example usage:
# result = count_divisible_digits(12)
# print(result)

# method 2 for gfg

class Solution:
    def evenlyDivides(self, N):
        count = 0
        original_N = N  # Keep the original value of N to perform division
        while N > 0:
            digit = N % 10  # Extract the last digit
            N = N // 10  # Remove the last digit
            if digit != 0 and original_N % digit == 0:  # Check for non-zero digits and divisibility
                count += 1
        return count

# Example usage:
sol = Solution()
result = sol.evenlyDivides(12)
print(result) 