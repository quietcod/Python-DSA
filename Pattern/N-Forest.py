# Problem statement
# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

# For every value of ‘N’, help sam to print the corresponding N-dimensional forest.

# Example:
# Input: ‘N’ = 3

# Output: 
# * * *
# * * *
# * * *

# Method 1
 
# N = int(input("Enter the value of N: "))

# for i in range(N):
#     print("* " * N)

# Method 2

def nForest(n: int) -> None:
    print(("* " * n + "\n") * n)

nForest(3)