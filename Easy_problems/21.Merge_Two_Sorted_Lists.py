# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Merges two sorted linked lists into a single sorted linked list.

        :type list1: Optional[ListNode] - The head of the first sorted linked list.
        :type list2: Optional[ListNode] - The head of the second sorted linked list.
        :rtype: Optional[ListNode] - The head of the merged sorted linked list.
        """

        # Create a dummy node to serve as the starting point of the merged list.
        dummy = ListNode()
        current = dummy  # Pointer to build the merged list

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move to the next node in the merged list

        # If any nodes remain in either list, append them to the merged list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the head of the merged list (dummy.next skips the dummy node)
        return dummy.next


"""
Workflow:
1. Initialize a dummy node and a pointer `current` to build the merged list.
2. Compare the heads of `list1` and `list2`:
   - Append the smaller value to the merged list.
   - Move the pointer of the smaller list forward.
3. Continue until one of the lists is exhausted.
4. Append any remaining nodes from the non-empty list.
5. Return `dummy.next` as the merged list's head.

Time Complexity: O(m + n)
   - We traverse both lists once, where `m` and `n` are the lengths of `list1` and `list2`.

Space Complexity: O(1)
   - We modify the existing lists without using extra space (other than a few pointers).
"""
