# Problem statement
# Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the Reverse N-Number Triangle.

# Example:
# Input: ‘N’ = 3

# Output: 

# 1 2 3
# 1 2
# 1

def nNumberTriangle(n: int) -> None:
    for i in range(n):
        for j in range(1, n - i + 1):
            print(j, end=" ")
        print()
nNumberTriangle(3)
