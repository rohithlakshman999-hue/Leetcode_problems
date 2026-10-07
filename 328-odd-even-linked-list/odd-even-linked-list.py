class Solution(object):
    def oddEvenList(self, head):
        ans=[]
        temp=head
        a=1
        while temp is not None:
            if a%2!=0:
                ans.append(temp.val)
            a+=1
            temp=temp.next
        
        temp=head
        b=1
        while temp is not None:
            if b%2==0:
                ans.append(temp.val)
            b+=1
            temp=temp.next
        
        temp=head
        i=0
        while temp is not None:
            temp.val = ans[i]
            i+=1
            temp = temp.next
        return head