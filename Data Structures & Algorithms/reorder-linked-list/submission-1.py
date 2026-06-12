# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return
        if head.next.next == None:
            return 

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None
        prev = slow
        while middle.next != None:
            next_node = middle.next
            middle.next = prev
            prev = middle
            middle = next_node
        
        middle.next = prev

        start = head
        end = middle

        while end.next != None:
            start_next = start.next
            start.next = end
            start = start_next
            end_next = end.next
            end.next = start
            end = end_next
    
        












        