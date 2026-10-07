class Solution(object):
    def reverseList(self, head):
        temp=head
        a=[]
        while temp is not None:
            a.append(temp.val)
            temp=temp.next

        a.reverse()
        temp=head
        i=0
        while temp is not None:
            temp.val=a[i]
            i+=1
            temp=temp.next
        return head
        
        

        