# Encode and Decode Strings 
# Question - Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and decoded back to the original list of strings.
# Implement Encode and Decode

# Solution 

def encode(self, strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(self, strs):
    res, i = [], 0
    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res