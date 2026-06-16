# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while True:
            found = False
            min_list = None
            for i in range(len(lists)):
                if lists[i] == None:
                    continue
                found = True
                min_list = i if (min_list == None or lists[i].val < lists[min_list].val) else min_list
            
            if found == False:
                break

            curr.next = lists[min_list]
            lists[min_list] = lists[min_list].next
            curr = curr.next
        
        return dummy.next

            
                
                    

        