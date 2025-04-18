# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        if n == length:
            return head.next
            
        cur = head
        for i in range(length - n - 1):
            cur = cur.next
        if cur and cur.next:
            cur.next = cur.next.next
        else:
            cur.next = None
        return head
        
        
        
        