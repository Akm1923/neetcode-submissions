# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        lst=[]

        for head in lists:
            curr=head
            while curr:
                lst.append(curr.val)
                curr=curr.next
            
        lst.sort()

        head=ListNode(lst[0])
        curr=head
        for i in range(1,len(lst)):
            curr.next=ListNode(lst[i])
            curr=curr.next
        return head

        



        

        