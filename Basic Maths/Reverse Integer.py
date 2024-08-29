# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_x = int(str(x)[::-1])
        reversed_x *= sign
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        return reversed_x
# Example usage:
sol = Solution()
print(sol.reverse(123))    # Output: 321
print(sol.reverse(-123))   # Output: -321
print(sol.reverse(120))    # Output: 21
print(sol.reverse(0))      # Output: 0
print(sol.reverse(1534236469)) # Output: 0