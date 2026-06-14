# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst=[]
        curr=head
        while curr:
            lst.append(curr.val)
            curr=curr.next
        lst2=[]
        for i in range(0,len(lst),k):
            grp=lst[i:i+k]
            if len(grp)==k:
                lst2.extend(reversed(grp))
            else:
                lst2.extend(lst[i:])

        head=ListNode(lst2[0])
        curr=head

        for i in range(1,len(lst2)):
            curr.next=ListNode(lst2[i])
            curr=curr.next
        return head
