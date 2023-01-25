# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        N = 0
        while head:
            N += 1
            head = head.next            
        
        start = 0
        while root:
            if start == N//2:
                mid = root
            start += 1
            root = root.next
            
        return mid