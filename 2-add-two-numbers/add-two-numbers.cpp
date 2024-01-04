class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* dummyNode = new ListNode(0);
    ListNode* curr = dummyNode;
    int carry = 0;
    while(l1 != NULL || l2!= NULL || carry != 0) 
    {
        int x = l1?l1->val:0;
        int y = l2?l2->val:0;
        int sum = carry+x+y;
        carry = sum / 10;
        curr->next = new ListNode(sum % 10);
        l1 = l1?l1->next : NULL;
        l2 = l2?l2->next:NULL;
        curr = curr->next;
    }
    return dummyNode->next;
    }
};