/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        map<ListNode*,int>map;
        ListNode* temp=headA;
        while(temp!=nullptr){
            map[temp]=1;
            temp=temp->next;
        }

        temp=headB;
        while(temp!=nullptr){
            if(map.find(temp)!=map.end()){
                return temp;
            }
            temp=temp->next;
        }
        return nullptr;
    }
};