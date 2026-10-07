class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* temp=head;
        ListNode* prev = nullptr;
        while (temp!=nullptr){
            ListNode* new_node = temp->next;
            temp->next=prev;
            prev=temp;
            temp=new_node;
        }
        return prev;
    }
};