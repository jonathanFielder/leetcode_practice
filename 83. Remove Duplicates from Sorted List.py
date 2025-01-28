# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        j = head
        while j:
            j = j.next
            if j:
                while j and j.val == i.val:
                    j = j.next
            i.next = j
            i = j
        return head
        
