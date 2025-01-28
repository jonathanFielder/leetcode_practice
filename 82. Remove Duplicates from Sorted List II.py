# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
           
            current = head
            prev = head
            while current:
                if current.next and current.val == current.next.val:
                    while current.next and current.val == current.next.val:
                        current = current.next
                    prev.next = current.next
                    if current.val == head.val:
                        head = current.next
                        prev = head
                else:
                    prev = current
                current = current.next

                   
        return head
            
        
