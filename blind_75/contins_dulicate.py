# Question - Given a integer array nums, return true if any value appers atleat twice in the array, and return false if every element is distinct.

# Solution 

# Bruteforce approach 
# Time Complexity - O(n^2)
# Space - O(1)

# sorting approach  - duplicats are adjacents (next to each other) hemce reduced time coplexity.
# Time Complexity - O(nlogn)
# Space - O(1)

# best case --
# Hash Set approch - add value to hash map while also checking for dulicates at the same time.
# Time Complexity - O(n) 
# Space - O(n) - Compromised here, but it dosen't matter our focus is time complexity.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False