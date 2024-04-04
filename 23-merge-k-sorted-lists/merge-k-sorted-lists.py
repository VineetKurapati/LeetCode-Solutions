# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2):
        # Logic to merge two linked lists
        curr = dummy = ListNode()
        while list1 and list2:
            if list2.val > list1.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next 
        # Append the remaining nodes from list1 or list2
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None 
        if k == 1:
            return lists[0]
        first_list = lists[0]
        for i in range(1, k):
            first_list = self.merge(first_list, lists[i])
        return first_list

