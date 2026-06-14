class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        vals = []

        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        ans = []
        left, right = 0, len(vals) - 1

        while left < right:
            ans.append(vals[left])
            ans.append(vals[right])
            left += 1
            right -= 1

        if left == right:
            ans.append(vals[left])

        curr = head
        i = 0

        while curr:
            curr.val = ans[i]
            i += 1
            curr = curr.next