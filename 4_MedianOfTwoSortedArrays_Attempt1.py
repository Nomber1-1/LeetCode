class Solution(object):
    def getMedian(self, nums): # Gets median of an array in O(1)
        size = len(nums)
        if size == 0 :
            return 0
        if size % 2 != 0:
            return nums[size//2]
        else:
            return (float(nums[size//2-1] + nums[size//2])) / 2

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sortedNums = []
        i = 0
        j = 0
        size1 = len(nums1)
        size2 = len(nums2)
        
        while i < size1 and j < size2:
            if (nums1[i] < nums2[j] or nums1[i] == nums2[j]):
                sortedNums.append(nums1[i])
                i += 1
            else:
                sortedNums.append(nums2[j])
                j += 1
        
        while i < size1:
            sortedNums.append(nums1[i])
            i += 1
        
        while j < size2:
            sortedNums.append(nums2[j])
            j += 1
        
        return self.getMedian(sortedNums)

    

if __name__ == "__main__":
    s = Solution()
    nums1, nums2 = [1,3], [2]
    print(s.findMedianSortedArrays(nums1,nums2))
    
    nums1, nums2 = [1,2], [3,4]
    print(s.findMedianSortedArrays(nums1,nums2))