# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr=[]
        while head is not None:
            arr.append(head.val)
            head=head.next
        left-=1
        right-=1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        temp=None
        temp2=None
        for i in arr:
            node= ListNode(i)
            if temp is None:
                temp=node
                temp2=node
            else:
                temp2.next=node
                temp2=node
        return temp
        