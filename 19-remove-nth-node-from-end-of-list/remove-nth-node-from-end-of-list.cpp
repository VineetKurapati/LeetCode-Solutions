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
    int length(ListNode* head)
    {
        int count = 0;
        while(head)
        {
            count += 1;
            head = head->next;
        }
        return count;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int k = length(head);
        k -= n;
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* ans = dummy;
        while(k-- && dummy)
        {
            dummy = dummy->next;
        }
        dummy->next = dummy->next->next;
        return ans->next;
    }
};