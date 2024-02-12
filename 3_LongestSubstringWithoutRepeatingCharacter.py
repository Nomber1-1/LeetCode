def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    longest_substr = ""
    temp_longest_substr = ""
    
    i = 0
    while(i < len(s)):
        if (temp_longest_substr.count(s[i]) != 0):
            if (len(temp_longest_substr) > len(longest_substr)):
                longest_substr = temp_longest_substr
            temp_longest_substr = temp_longest_substr[temp_longest_substr.index(s[i])+1::1]
        temp_longest_substr += s[i]
        i += 1
        
    if (len(temp_longest_substr) > len(longest_substr)):
        longest_substr = temp_longest_substr
        
    print(longest_substr)
    return len(longest_substr)

""" - ALTERNATE SOLUTION -
def lengthOfLongestSubstring(self, s):
        seen={}
        l=0
        length=0
        for r in range(len(s)):
            char=s[r]
            if char in seen and seen[char]>=l:
                l=seen[char]+1
            else:
                length=max(length,r-l+1)
            seen[char]=r
        return length
"""
    
if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s)) # 3 -> abc
    
    s = "bbbbb"
    print(lengthOfLongestSubstring(s)) # 1 -> b
    
    s = "pwwkew"
    print(lengthOfLongestSubstring(s)) # 3 -> wke
    
    s = "dvdf"
    print(lengthOfLongestSubstring(s)) # 3 -> vdf
        