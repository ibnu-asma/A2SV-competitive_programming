# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        count = 1
        cur = head
        while cur.next:
            count += 1
            cur = cur.next
        cur.next = head
        k = k % count
        
        temp  = head
        for i in range(count - k - 1):
            temp = temp.next

        prefix = temp.next
        temp.next = None

        return prefix
