# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        num1 = 0
        while cur:
            num1  = (num1 * 10) + cur.val
            cur = cur.next
        
        cur = l2
        num2 = 0
        while cur:
            num2  = (num2 * 10) + cur.val
            cur = cur.next

        total = num1 + num2
        dummy = ListNode()
        cur = dummy
        while total > 0:
            digit = total % 10
            cur.next = ListNode(digit)
            total = total // 10
            cur = cur.next
        
        temp = dummy.next
        prev = None

        while temp:
            cur_temp = temp.next
            temp.next = prev
            prev = temp
            temp = cur_temp
        return prev if dummy.next else ListNode()
        