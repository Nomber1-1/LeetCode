def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1

    return index

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    print(removeElement(nums, val))