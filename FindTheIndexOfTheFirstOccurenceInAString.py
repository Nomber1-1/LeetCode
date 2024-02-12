class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        size_n = len(needle)
        size_h = len(haystack)

        if haystack.count(needle) == 0:
            return -1
    
        i = 0
        j = 0
        
        while i < size_h - size_n + 1:
            print(haystack[i])
            if haystack[i] == needle[0]:
                temp = ""
                for j in range(size_n):
                    temp += haystack[i+j]
                if temp == needle:
                    return i
            i += 1
            
        return temp
    
    """ - Alternative Solution -
    class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i+len(needle)] == needle:
                return i        
        return -1
    """
        
if __name__ == "__main__":
    s = Solution()
    haystack = "mississippi"
    needle = "issip"
    print(s.strStr(haystack, needle))