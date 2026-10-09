class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* temp=head;
        int n=0;
        while (temp!=nullptr){
            temp=temp->next;
            n++;
        }
        int a=n/2;
        temp=head;
        while(a>0){
            temp=temp->next;
            a--;
        }
        return temp;
    }
};