# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1=[]
        curr1=l1
        while curr1:
            a1.append(curr1.val)
            curr1=curr1.next
        a2=[]
        curr2=l2
        while curr2:
            a2.append(curr2.val)
            curr2=curr2.next
        a1.reverse()
        a2.reverse()
        a1=[str(x) for x in a1]
        a2=[str(x) for x in a2]

        opr1="".join(a1)
        opr2="".join(a2)
        res=list(str(eval(opr1+'+'+opr2)))
        res.reverse()

        head2=ListNode(res[0])
        curr=head2
        for i in range(1,len(res)):
            curr.next=ListNode(res[i])
            curr=curr.next
        curr.next=None

        return head2





        

        