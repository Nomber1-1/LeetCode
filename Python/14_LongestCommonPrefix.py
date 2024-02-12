def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
        
    longest_common = ""
        
    if (len(strs) == 1):
        return strs[0]
        
    for i in range(len(strs)):
        temp_common = ""
        first_word  = strs[i]
            
        if (i==0):
            second_word = strs[i+1]
        else:
            second_word = longest_common
                
        j = 0          
        while(j < len(first_word) and j < len(second_word) and first_word[j] == second_word[j]):
            temp_common += first_word[j]
            j += 1
            
        if longest_common == "" or len(temp_common) < len(longest_common):
            longest_common = temp_common
                
    return longest_common
    
    """ Alternate Solution
     final = ""
        strs.sort()
        length = min(len(strs[0]) , len(strs[len(strs) - 1]))

        i = 0
        while (i < length and strs[0][i] == strs[len(strs) - 1][i]):
            i+=1
        
        return strs[0][0:i]
    """
            
                        
if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))
    
    strs = ["dog","racecar","car"]
    print(longestCommonPrefix(strs))