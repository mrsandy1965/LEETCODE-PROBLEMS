# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sl=head
        fast=head
        for _ in range(10**6):
            if not fast or not fast.next:
                return False
            sl=sl.next
            fast=fast.next.next
            if sl==fast:
                return True