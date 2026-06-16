# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 and l2:
            summ = l1.val + l2.val + carry 
            carry = summ // 10
            curr.next = ListNode(summ%10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            summ = l1.val + carry
            carry = summ // 10 
            curr.next = ListNode(summ%10)
            l1 = l1.next
            curr = curr.next
        
        while l2: 
            summ = l2.val + carry
            carry = summ // 10 
            curr.next = ListNode(summ%10)
            l2 = l2.next
            curr = curr.next
        
        if carry:
            curr.next = ListNode(carry)
            curr = curr.next
        
        return dummy.next




        