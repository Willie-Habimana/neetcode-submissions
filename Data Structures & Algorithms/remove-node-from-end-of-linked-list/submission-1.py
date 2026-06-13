# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        curr = head
        while curr.next != None:
            curr = curr.next
            count += 1
        
        if count == 1:
            return None
        
        if n == 1:
            curr = head
            while curr.next.next != None:
                curr = curr.next

            curr.next = None
            return head 
    
        
        remove_index = count - n

        if remove_index == 0:
            return head.next

        curr = head 
        i = 1
        while i < remove_index:
            curr = curr.next
            i += 1
        
        curr.next = curr.next.next

        return head
        



        