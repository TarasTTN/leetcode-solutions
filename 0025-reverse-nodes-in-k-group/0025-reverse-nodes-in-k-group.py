# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        def get_kth(curr: ListNode | None, k: int) -> ListNode | None:
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break

            group_next = kth.next

            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            next_group_prev = group_prev.next
            group_prev.next = kth
            group_prev = next_group_prev

        return dummy.next