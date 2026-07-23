# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list_test = []
        start = head
        res = False
        if start == None:
            return False
        while start.next != None:
            if start.next in list_test:
                res = True
                break
            else:
                list_test.append(start)
                start = start.next

        return res
        
