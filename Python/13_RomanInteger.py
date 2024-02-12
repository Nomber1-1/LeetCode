
def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        decimal_val = 0
        
        length = len(s)
        
        i = 0
        while (i < len(s)):
            first = roman_dict.get(s[i])
            
            if (i < len(s)-1):
                second = roman_dict.get(s[i+1]) 
                if (first < second):
                    decimal_val += (second - first)
                    i += 2
                    continue

            decimal_val += first
            i += 1
        
        return decimal_val
    
    """ Another Splution
    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0

        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                res += roman[s[i]] - 2*roman[s[i - 1]]
            else:
                res += roman[s[i]]
        
        return res
    """
                
if __name__ == "__main__":
    s = "III" #3
    print(romanToInt(s))
    s = "LVIII" #58
    print(romanToInt(s))
    s = "MCMXCIV" #1994
    print(romanToInt(s))