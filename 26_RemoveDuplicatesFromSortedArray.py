def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Solution from: https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/2107606/py-all-4-methods-intuitions-walk-through-wrong-answer-explanations-for-beginners-python/
    """
    nums[:] = sorted(set(nums))
    return len(nums)
    """
    
    # Alternative Solution - Two-pointers
    slow, fast = 0, 1
    while fast in range(len(nums)):
        if nums[slow] == nums[fast]: # Found duplicate -> Keep going until find unique
            fast += 1
        else:
            nums[slow+1] = nums[fast] # Found unique -> Move Slow to next index and replace it by fast value
            fast += 1
            slow += 1
    
    return slow + 1 # + 1 because doesn't count first unique (can't be 0 since array size of min 1)

if __name__ == "__main__":
    nums = [1,1,2]
    print(removeDuplicates(nums))