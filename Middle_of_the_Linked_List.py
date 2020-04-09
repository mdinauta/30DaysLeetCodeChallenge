# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class BruteForceSolution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list_length = 1
        cur = head
        while cur.next is not None:
            list_length += 1
            cur = cur.next

        middle_node_index = list_length // 2

        cur = head
        i = 0
        while i < middle_node_index:
            cur = cur.next
            i += 1

        return cur

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        single = head
        double = head
        while double and double.next:
            single = single.next
            double = double.next.next

        return single