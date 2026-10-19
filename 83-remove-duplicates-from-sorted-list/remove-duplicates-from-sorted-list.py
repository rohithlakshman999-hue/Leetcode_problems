class Solution(object):
    def deleteDuplicates(self, head):
        temp=head
        while temp is not None and temp.next is not None:
            if temp.val==temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
        