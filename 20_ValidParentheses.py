def isValid(s):
        stack = []

        if (s.count("(") != s.count(")")):
            return False
        if (s.count("{") != s.count("}")):
            return False
        if (s.count("[") != s.count("]")):
            return False

        for i in range(len(s)):
            par = s[i]

            if par == "(":
                stack.append(par)
            if par == ")":
                if stack.count("(")==0:
                    return False
                open_par = stack.pop()
                if open_par != "(":
                    return False
            
            if par == "{":
                stack.append(par)
            if par == "}":
                if stack.count("{")==0:
                    return False
                open_par = stack.pop()
                if open_par != "{":
                    return False
            
            if par == "[":
                stack.append(par)
            if par == "]":
                if stack.count("[")==0:
                    return False
                open_par = stack.pop()
                if open_par != "[":
                    return False
        
        return len(stack)==0
    
""" - Alternative Solution -

        matches = {")": "(", "]": "[", "}": "{"}

        if len(s) < 2 or s[0] in matches:
            return False

        stack = []

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
                continue

            if len(stack) <= 0:
                return False

            if stack[-1] == matches[bracket]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
"""

    
if __name__ == "__main__":
    s = "(){}}{"
    print(isValid(s))