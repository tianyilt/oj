# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # from copy import deepcopy
        dummy = ListNode()
        node = dummy
        # dummy.next = node
        while list1 and list2:
            v1=list1.val
            v2=list2.val
            
            if v1 > v2:
                node.next = ListNode(v2)
                
                # if list2.next:
                list2 = list2.next
                # v2 = list2.val
                # else:
                #     break
            else:
                node.next = ListNode(v1)
                
                # if list1.next:
                list1 = list1.next
                # v1 = list1.val
                # else:
                #     break
                # remain = list1 or list2
            node = node.next
        remain = list1 or list2
        while remain:
            node.next = ListNode(remain.val)
            node = node.next
            remain = remain.next

        return dummy.next

so = Solution()
print(so.mergeTwoLists([1,2,4],[1,3,4]))