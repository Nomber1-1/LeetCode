import doctest

def twoSum(self, nums, target):
    """
    
    >>> twoSum(0, [3, 1, 4], 5)
    (1, 2)
    
    >>> twoSum(0, [3, -1, -4], -5)
    (1, 2)

    >>> twoSum(0, [0, 4, 3, 0], 0)
    (0, 3)
    
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    
    """
   
    for i in range(0,len(nums)):            
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    return i,j
            
        
if __name__ == "__main__":
    doctest.testmod()