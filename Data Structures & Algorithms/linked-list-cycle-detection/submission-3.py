# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        slow = head.next
        fast = head.next.next

        while slow != None and slow.next != None and fast != None and fast.next != None and slow != fast:
            slow = slow.next
            fast = fast.next.next

        
        return slow == fast
        

        