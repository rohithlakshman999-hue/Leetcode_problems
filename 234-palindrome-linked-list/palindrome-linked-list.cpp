class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* temp=head;
        stack <int>a;
        while (temp!=nullptr){
            a.push(temp->val);
            temp=temp->next;
        }
        temp=head;
        while(temp!=nullptr){
            if(temp->val!=a.top()){
                return false;
            }
            a.pop();
            temp=temp->next;
        }
        return true;
    }
};