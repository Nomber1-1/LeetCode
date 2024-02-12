def reverse(x):
    """
    :type x: int
    :rtype: int
    """
        
    sign = 1 
    if(x < 0):
        sign = -1
        x = x * -1
    
    reversed_num = 0
    temp = x

    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
    
    if reversed_num < -(2**31) or reversed_num > 2**31-1:
        return 0
    
    return reversed_num * sign

if __name__ == "__main__":
    x = 123 #321
    print(reverse(x))
    x = -321 #-123
    print(reverse(x))
    x = 120 #21
    print(reverse(x))