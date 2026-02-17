# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # find the length of A and B 
        lenA , lenB =1, 1 
        currA ,currB = headA ,headB

        while currA.next:
            lenA += 1
            currA = currA.next

        while currB.next :
            lenB += 1
            currB = currB.next 

        diff = abs(lenA - lenB)

        if lenA > lenB:
            while diff:
                headA = headA.next
                diff -=1
        elif lenB > lenA:
            while diff:
                headB = headB.next
                diff -=1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA                    
            