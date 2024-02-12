import doctest

def twoSum(self, nums, target):
    """
    >>> twoSum(0, [1, 3, 4], 3)
    [1]
    
    >>> twoSum(0, [3, 1, 4], 5)
    [1, 2]
    
    >>> twoSum(0, [3, -1, -4], -5)
    [1, 2]
    
    >>> twoSum(0, [0, 4, 3, 0], 0)
    [0, 3]
    
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    
    1. Use self as reference
    2. Check if correct answer:
        2.1. If yes, return self
        2.2. If no, check if next number.
    3. If exists, add next number.
        3.1. If correct answer, return positions.
        3.2. If not try adding self and next number.
    4. If not, try adding one more number, etc.
    
    """
    for i in range(0,len(nums)):
        listOfIndexes = [] 
        # Base Case: The target is in nums
        if (nums[i] == target and target != 0):
            listOfIndexes.append(i);
            return listOfIndexes
        
        # Inductive Step 1: Check if sum of 2
        for j in range(len(nums)):
            if (j != i):
                sum_2 = nums[i] + nums[j]
                if (sum_2 == target):
                    listOfIndexes.append(i)
                    listOfIndexes.append(j)
                    return listOfIndexes;
    
if __name__ == "__main__":
    doctest.testmod()