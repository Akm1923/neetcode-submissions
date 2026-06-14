class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        vals = []

        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        vals.pop(len(vals) - n)

        if not vals:
            return None

        newHead = ListNode(vals[0])
        curr = newHead

        for i in range(1, len(vals)):
            curr.next = ListNode(vals[i])
            curr = curr.next

        return newHead