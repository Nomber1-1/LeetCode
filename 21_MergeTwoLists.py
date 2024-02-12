class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        head = ListNode()
        current = head
        arrayview = []
        
        if list1 == None and list2 == None:
            return None 
        
        while list1 != None or list2 != None:
            if list1 != None and list2 != None:
                if list1 != None and (list1.val < list2.val or list1.val == list2.val):
                    current.next = list1
                    list1 = list1.next
                    
                else:
                    current.next = list2
                    list2 = list2.next                 
                current = current.next
                arrayview.append(current.val)
                
            else:
                
                while list1 != None and list2 == None:
                    current.next = list1
                    list1 = list1.next
                    current = current.next
                    
                while list2 != None and list1 == None:
                    current.next = list2
                    list2 = list2.next
                    current = current.next
            
        print(arrayview)
        
        return head.next
    
""" - Alternative -
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        '''
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        '''
        NewList = ListNode()

	def Merge(NewList,node1,node2):
			if node1 == None and node2 == None:
				return
			if node1 == None and node2 != None:
				return node2
			if node2 == None and node1 != None:
				return node1
			if node1.val <= node2.val:
				NewList = node1
				NewList.next = Merge(NewList, node1.next,node2)
			if node1.val > node2.val:
				NewList = node2
				NewList.next = Merge(NewList, node1,node2.next)
			return NewList
	return Merge(NewList,list1,list2)
"""

""" - Alternative -
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)  
        cur = dummy  
        while l1 and l2:  
            if l1.val <= l2.val:  
                cur.next = l1  
                l1 = l1.next  
            else:  
                cur.next = l2  
                l2 = l2.next  
            cur = cur.next  
        cur.next = l1 or l2  
  
        return dummy.next
"""

if __name__ == "__main__":
    list1_node1 = ListNode(1)
    list1_node2 = ListNode(2)
    list1_node3 = ListNode(4)
    
    list1_node1.next = list1_node2
    list1_node2.next = list1_node3
    
    list2_node1 = ListNode(1)
    list2_node2 = ListNode(3)
    list2_node3 = ListNode(4)
    
    list2_node1.next = list2_node2
    list2_node2.next = list2_node3
    
    head = mergeTwoLists(list1_node1,list2_node1)
    
    while (head != None):
        print(head.val)
        head = head.next