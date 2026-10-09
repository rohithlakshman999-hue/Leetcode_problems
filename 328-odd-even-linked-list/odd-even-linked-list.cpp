class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode* temp=head;
        vector<int> ans;
        int n=1;
        while (temp!=nullptr){
            if(n%2!=0){
                ans.push_back(temp->val);
            }
            n++;
            temp=temp->next;
        }
        temp=head;
        int a=1;
        while(temp!=nullptr){
            if (a%2==0){
                ans.push_back(temp->val);
            }
            a++;
            temp=temp->next;
        }
        temp=head;
        int i=0;
        while (temp!=nullptr){
            temp->val=ans[i];
            i++;
            temp=temp->next;
        }

        return head;
    }
};