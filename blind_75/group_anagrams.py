# Question - Given an array of strings strs, group the anagram together. You can return the answer in any order.

# Solution 

# time complexity - O(m*n) 

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a to z

            for c in s:
                count[ord(c) - ord("a")] += 1 # subracting the ascii value of current order from order (a) 
            res[tuple(count)].append(s)
        return res.values()
