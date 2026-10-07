class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int a=0;
        ListNode* temp=head;
        while(temp!=nullptr){
            a+=1;
            temp=temp->next;
        }
        int r=1;
        temp=head;
        int b = a - n;
         if(b == 0){
            return head->next;
        } 
        while(temp!=nullptr){
            if(r==b){
                temp->next = temp->next->next;
                break;
            }
            r++;
            temp=temp->next;
        }
        return head;
    }
};