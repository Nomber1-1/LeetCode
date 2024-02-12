import doctest
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        >>> l1 = [2,4,3]
        >>> l2 = [5,6,4]
        >>> addTwoNumbers(self, l1, l2)
        [7,0,8]
        
        >>> l1 = [0], l2 = [0]
        [0]
        
        >>> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        [8,9,9,9,0,0,0,1]
        
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_o = []
        l2_o = []
        len1 = 0
        len2 = 0
        n1 = ""
        n2 = ""
        
        #Get length of SLL:
        while l1.next != None:
            len1 += 1
        while l2.next != None:
            len2 += 1

        while(len1 != 0):
            for i in range[len1]:
                l1.next
            n1 += l1.val
            len1 -= 1
        print(n1)

        while(len2 != 0):
            for i in range[len2]:
                l2.next
            n2 += l2.val
            len2 -= 1
        print(n2)
        
        return 1

if __name__ == "__main__":
    doctest.testmod()