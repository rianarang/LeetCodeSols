# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        head = node
        prev = node
        while head.next:
            head.val = head.next.val
            prev = head
            head = head.next
        
        prev.next = None