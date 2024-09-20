# Question - Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Solution 
# anagram meaning - means the word stored in s and t should be same, same in size/length, no. of duplicate characters, it does not matter how they are spelled.

# time complexity - O(n) or O(s + t)

# 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, CountT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            CountT[t[i]] = 1 + CountT.get(t[i], 0)
        for c in countS:
            if countS[c] != CountT.get(c, 0):
                return False
        return True
    
# 2 - may not work in interview but works on leetcode

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
# 3 - sorting approach - increses time compexity - bad case - n^2, better case - nlogn
# not as good as aboce two solutions.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
