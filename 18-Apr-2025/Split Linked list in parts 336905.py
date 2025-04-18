# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        base = length // k
        extra = length % k

        cur = head
        result = []
        for i in range(k):
            part_head = cur
            part_size = base + (1 if extra > 0 else 0)
            extra -= 1

            for i in range(part_size - 1):
                if cur:
                    cur = cur.next

            if cur:
                next_part = cur.next
                cur.next = None
                cur = next_part

            result.append(part_head)


        return result

        