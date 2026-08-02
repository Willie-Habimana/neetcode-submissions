# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        count = len(lists)
        while count > 0:
            minIndex = 0
            for i in range(1, len(lists)):
                if lists[minIndex] == None or (lists[i] and lists[i].val < lists[minIndex].val):
                    minIndex = i
            curr.next = lists[minIndex]
            curr = curr.next
            lists[minIndex] = lists[minIndex].next
            if lists[minIndex] == None:
                count -= 1
        return dummy.next



            
                
                    

        