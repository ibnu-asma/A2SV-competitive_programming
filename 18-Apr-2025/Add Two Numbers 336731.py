# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        cur =head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur =  temp
        return prev
    def sum(self, head):
        cur = head
        total = 0
        while cur:
            total = (total*10) + cur.val
            cur = cur.next
        return total


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_rev = self.reverse(l1)
        l2_rev = self.reverse(l2)

        total  = self.sum(l1_rev) + self.sum(l2_rev)
        dummy = ListNode(0)
        cur = dummy
        while total > 0:
            digit = total%10
            cur.next = ListNode(digit) 
            total = total//10
            cur = cur.next
        
        return dummy.next if dummy.next else ListNode(total)


        
        
        

        


        