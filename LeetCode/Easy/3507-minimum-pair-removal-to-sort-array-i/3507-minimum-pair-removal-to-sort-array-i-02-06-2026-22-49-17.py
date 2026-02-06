class Node:
    def __init__(self, _next, val):
        self.next = _next
        self.val = val

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        head = Node(None, 0)
        res = 0

        cur = head
        for num in nums:
            cur.next = Node(None, num)
            cur = cur.next
        
        while True:
            is_ascending = True
            cur = head
            
            min_sum = float('+inf')
            prev = Node(None, 0)
            while cur.next.next:
                if cur.next.val > cur.next.next.val:
                    is_ascending = False
                
                if (cur.next.val + cur.next.next.val) < min_sum:
                    min_sum = cur.next.val + cur.next.next.val
                    prev = cur
                
                cur = cur.next
            
            if is_ascending:
                break

            tmp = Node(None, prev.next.val + prev.next.next.val)
            last = prev.next.next
            prev.next = tmp
            tmp.next = last.next

            res += 1

        return res