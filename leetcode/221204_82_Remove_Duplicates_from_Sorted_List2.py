# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h = head
        check = []
        ans = []
        while h:
            check.append(h.val)            
            h = h.next
        
        cc = Counter(check)
        
        # print(cc)
        
        for k, v in cc.items():
            if v == 1:
                ans.append(k)   
        
        if len(ans) == 0:
            return ListNode().next
        
        rtn = ListNode(ans[0]) 
        s = rtn
        
        for i in range(1, len(ans)):                
            rtn.next = ListNode(ans[i])
            rtn = rtn.next
            
        return s