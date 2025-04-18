# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = head, head
        while cur:
            if cur.val !=  prev.val:
                prev.next = cur
                prev = prev.next
            cur = cur.next
        if prev:
            prev.next = None
        return head
                
        