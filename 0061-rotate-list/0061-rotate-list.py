# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None or k == 0:
            return head
        temp = head
        n = 1
        while temp.next is not None:
            temp = temp.next
            n += 1
        k = k % n
        if k == 0:
            return head
        temp.next = head
        steps = n - k
        temp = head
        for i in range(steps - 1):
            temp = temp.next
        head = temp.next
        temp.next = None
        return head