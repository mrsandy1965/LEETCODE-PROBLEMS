# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.traverse(root, head)
    def traverse(self, thead, lhead):
        if not thead:
            return False
        
        if self.checkPath(thead, lhead):
            return True
        return self.traverse(thead.left, lhead) or self.traverse(thead.right, lhead)
        
    def checkPath(self, thead, lhead):
        if not lhead:
            return True
        if not thead:
            return False
        if thead.val != lhead.val:
            return False
        
        return self.checkPath(thead.left, lhead.next) or self.checkPath(thead.right, lhead.next)