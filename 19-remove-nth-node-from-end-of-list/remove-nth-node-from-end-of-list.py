class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        a=0
        while temp is not None:
            temp=temp.next
            a+=1
        
        b=a-n
        r=1
        if b==0:
            return head.next
        temp=head

        while temp is not None:
            if r==b:
                temp.next=temp.next.next
                break
            r+=1
            temp=temp.next
        return head
        