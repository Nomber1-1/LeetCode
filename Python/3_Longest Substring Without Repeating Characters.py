class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = list(s)
        repeated_letters = []
        longest_length = 0

        for i in range(0, len(s1)):
            if (s1[i].isspace() and repeated_letters.count(" ") == 0):
                repeated_letters.append(" ")
            elif (repeated_letters.count(s1[i]) == 0):
                repeated_letters.append(s1[i])
            else:
                current_length = len(repeated_letters)
                repeated_letters = []
                if (longest_length <= current_length):
                    longest_length = current_length
                repeated_letters.append(s1[i])
        return longest_length

g = Solution
print(g.lengthOfLongestSubstring(g, " "))