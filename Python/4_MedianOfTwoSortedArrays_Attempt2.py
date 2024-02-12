class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        Two pointers: smaller and bigger
        Increment them together until half the total elements have been seen
        Then calculate the median using the pointer values
        """
        
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0
        
        # Find median
        for count in range((n+m) // 2 + 1):
            m2 = m1
            if i < n and j < m:
                if nums1[i] < nums2[j]:
                    m1 = nums1[i]
                    i += 1
                else:
                    m1 = nums2[j]
                    j += 1
            elif i < n:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1
                
        # Check if the sum of n and m is odd.
        if (n + m) % 2 == 1:
            return float(m1)
        else:
            return (float(m1) + float(m2)) / 2.0

if __name__ == "__main__":
    s = Solution()
    nums1, nums2 = [1,3], [2]
    print(s.findMedianSortedArrays(nums1,nums2))
    
    nums1, nums2 = [1,2], [3,4]
    print(s.findMedianSortedArrays(nums1,nums2))
