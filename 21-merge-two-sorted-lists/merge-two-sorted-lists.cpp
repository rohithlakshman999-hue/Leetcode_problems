/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* temp=list1;
        vector<int> ans;
        while(temp!=nullptr){
            ans.push_back(temp->val);
            temp=temp->next;
        }

        temp=list2;
        while(temp!=nullptr){
            ans.push_back(temp->val);
            temp=temp->next;
        }
        sort(ans.begin(),ans.end());
        ListNode dummy(0);
        temp = &dummy;
        for(int i=0;i<ans.size();i++){
            temp->next=new ListNode(ans[i]);
            temp=temp->next;
        }
        return dummy.next;
    }
};