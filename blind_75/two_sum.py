# Question - Given an array of two integers nums and an integer target, return indices of the two numbers such that they ad upo to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Solution 

# 1. Bruteforce approach - worst case 
# time complexity - O(n^2)

# 2. hash map approach -  in this method we take the target value and subtract it to the current array value and store the solution in the hash table
#  and move to the next value, until we get the value that already exist in the array, then this values and the exixting value is our solution.

# time complexity - O(n)
# space complexity - O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return