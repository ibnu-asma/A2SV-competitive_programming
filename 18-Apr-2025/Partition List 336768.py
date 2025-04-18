# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        slist = ListNode()
        llist = ListNode()
        small, big = slist, llist
        cur = head
        while cur:
            if cur.val < x:
                small.next = ListNode(cur.val)
                small = small.next
            else:
                big.next = ListNode(cur.val)
                big = big.next
            cur = cur.next
        
        temp = slist
        while temp.next:
            temp = temp.next
        temp.next = llist.next

        return slist.next
        
            
         