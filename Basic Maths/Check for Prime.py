# Given an array arr[] of size n of non-negative integers. 
# Each array element represents the maximum length of the jumps that can be made forward from that element.
# This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
# Find the minimum number of jumps to reach the end of the array starting from the first element.
# If an element is 0, then you cannot move through that element.
# Note:  Return -1 if you can't reach the end of the array.

class Solution:
    def minJumps(self, arr, n):
        # If the array has only one element
        if n == 1:
            return 0
        
        # If the first element is 0, end cannot be reached
        if arr[0] == 0:
            return -1
        
        # Initialize maximum reach, steps, and jumps
        maxReach = arr[0]
        step = arr[0]
        jumps = 1
        
        # Traverse the array
        for i in range(1, n):
            # Check if we've reached the last element
            if i == n - 1:
                return jumps
            
            # Update the maximum reach
            maxReach = max(maxReach, i + arr[i])
            
            # Use a step to get to the current index
            step -= 1
            
            # If no more steps left
            if step == 0:
                # We must have used a jump
                jumps += 1
                
                # Check if the current index/position is beyond or equal to maxReach
                if i >= maxReach:
                    return -1
                
                # Re-initialize the steps to the amount of steps to reach maxReach
                step = maxReach - i
        
        return -1

# Example usage:
sol = Solution()
arr = [1, 4, 3, 2, 6, 7]
n = len(arr)
print(sol.minJumps(arr, n))  # Output: 3
