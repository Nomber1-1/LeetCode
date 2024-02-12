class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Expand from center method - 1719ms
        
        longest_palindrome = ""
        palindrome = ""
        left, right = '', ''
        j, k = 0, 0
        if len(s) == 1:
            return s[0]
        
        for i in range(len(s)):
            j = i - 1
            palindrome = s[i]
            while i < len(s)-1 and s[i] == s[i+1]:
                    palindrome = palindrome + s[i+1]
                    i += 1
            k = i+1
            
            while j >= 0 and k <= len(s)-1 and s[j] == s[k]:
                palindrome = s[j] + palindrome + s[k]
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome
                j -= 1
                k += 1
                
            j = i-1
            palindrome = s[i]
            while j >= 0 and s[j] == s[j+1]:
                palindrome = s[j] + palindrome
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome
                j -= 1
                
            k = i+1    
            palindrome = s[i]
            while k <= len(s)-1 and s[k-1] == s[k]:
                palindrome = palindrome + s[k]
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome
                k += 1
        
        if s != None and longest_palindrome == "":
            return s[0]
                
        return longest_palindrome
    
    def isPalindrome(self, s):
        # check if a string s is a palindrome
        if s[::-1] != s[::1]:
            return False
        return True 

    """ Shorter Expand from Center Version - 297ms
    class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str
    """
    
if __name__ == "__main__":
    sol = Solution()
    s = "azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc"
    print(sol.longestPalindrome(s))
    