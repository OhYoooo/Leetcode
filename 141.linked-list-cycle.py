# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # two pointer in O(1) memory
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast != slow and fast.next != slow:
            if not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
