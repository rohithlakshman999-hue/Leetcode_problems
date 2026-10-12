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
    ListNode* deleteMiddle(ListNode* head) {
        if(head->next==nullptr){
        return nullptr;
    }

    ListNode* temp=head;
    int i=0;
    while(temp!=nullptr){
        temp=temp->next;
        i++;
    }
    temp=head;
    int n=i/2;
    int b=0;
    while(b<n-1){
        b++;
        temp=temp->next;
    }
    temp->next=temp->next->next;
    return head;
    }
};