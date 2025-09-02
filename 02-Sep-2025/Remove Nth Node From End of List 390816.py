# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur, N  = head, 0
        while cur:
            N += 1
            cur = cur.next
        pos = N - n
        if pos == 0:
            return head.next
        cur = head
        for i in range(N - 1):
            if (i + 1) == pos:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head