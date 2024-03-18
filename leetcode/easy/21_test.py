class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node and a current node pointing to dummy
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists and compare each node
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remainder of list1 or list2
        current.next = list1 or list2

        # Return the merged list, skipping the dummy node
        return dummy.next

# Helper function to convert array to linked list
def arrayToList(arr):
    head = ListNode(0)
    current = head
    for number in arr:
        current.next = ListNode(number)
        current = current.next
    return head.next

# Helper function to print linked list
def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Test cases
solution = Solution()

# Convert arrays to linked lists
l1 = arrayToList([1,2,4])
l2 = arrayToList([1,3,4])

# Merge lists and print result
mergedList = solution.mergeTwoLists(l1, l2)
printList(mergedList)  # Expected output: 1 1 2 3 4 4

# Additional test cases
testCases = [
    ([], []),
    ([], [0])
]

for l1Arr, l2Arr in testCases:
    l1 = arrayToList(l1Arr)
    l2 = arrayToList(l2Arr)
    mergedList = solution.mergeTwoLists(l1, l2)
    printList(mergedList)
