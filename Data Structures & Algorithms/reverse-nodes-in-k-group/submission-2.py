# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        new_head = start = end = head
        found = False
        prev = None
        while True:
            i = 1
            while end != None and i < k:
                end = end.next
                i += 1
            
            if end == None:
                return new_head
            
            if prev:
                prev.next = end

            start_next = start.next
            start.next = end.next
            new_end = prev = start
            start = start_next
            while start != end:
                start_next = start.next
                start.next = prev
                prev = start
                start = start_next

            if found == False:
                new_head = end
                found = True

            end_next = end.next
            end.next = prev
            prev = new_end
            start = end = end_next
        return new_head
            
        


            
        
        