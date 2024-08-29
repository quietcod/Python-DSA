# Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD. 
# The function takes two integers a and b as input and returns a list containing their LCM and GCD.

class Solution:
    def gcd(self, A: int, B: int) -> int:
        while B:
            A, B = B, A % B
        return A
    
    def lcm(self, A: int, B: int) -> int:
        return abs(A * B) // self.gcd(A, B)
    
    def lcmAndGcd(self, A: int, B: int) -> list:
        gcd_value = self.gcd(A, B)
        lcm_value = self.lcm(A, B)
        return [lcm_value, gcd_value]

# Example usage:
sol = Solution()
result = sol.lcmAndGcd(12, 18)
print(result)  # Output: [36, 6]