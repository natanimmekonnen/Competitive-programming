# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
                
        c=ini= ListNode()
    
        while heap:
            v, i, node = heapq.heappop(heap)
            c.next = node
            c = c.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return ini.next
