# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy
        while True:
            kth = self.getkth(prevGroup, k)
            if not kth:
                break
            nextGroup = kth.next
            prev, cur = kth.next, prevGroup.next
            while cur != nextGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
        return  dummy.next

    def getkth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1

        return cur

        