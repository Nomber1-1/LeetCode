class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        
        for number in nums:
            if number in dict1:
                dict1[number] += 1
            else:
                dict1[number] = 1
        
        majority = (0,0)
        for key, value in dict1.items():
            if value > majority[1]:
                majority = (key, value)
        return majority[0]
    
    """ - Alternative Solution -
    .count with for val in nums()
    
    """

if __name__ == "__main__":
    s = Solution()
    nums = [2,2,1,1,1,2,2]
    print(s.majorityElement(nums))