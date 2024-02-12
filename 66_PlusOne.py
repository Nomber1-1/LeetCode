import math
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        
        while digits[i] == 9 and i > -1:
                digits[i] = 0
                i -= 1
        if i != -1:
            digits[i] += 1
        if digits[i] == 0:
            digits.insert(0, 1)
        
        result = ""
        for digit in digits:
            result += str(digit)
        
        return int(result)
        
        
        """
        # [1, 2, 3] = 1x100 + 2x10 + 3x1 = 1x10^2 + 2x10^1 + 2x10^0
        print(f"len is:",len(digits))
        num = 0
        for i in range(len(digits)-1,-1,-1):
            print(i)
            print(digits[len(digits) - i-1] * int(math.pow(10,i)))
            num += int(digits[len(digits) - i-1] * int(math.pow(10,i)))
            print(num)
        num = str(int(num+1))
        print(num)
        result = []
        for char in num:
            result.append(int(char))
        return result
        """
    
if __name__ == "__main__":
    s = Solution()
    digits  = [7,2,8,5,0,9,1,2,9,5,3,6,6,7,3,2,8,4,3,7,9,5,7,7,4,7,4,9,4,7,0,1,1,1,7,4,0,0,6]
    print(s.plusOne(digits))