# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr=[]
        temporary=head
        while temporary is not None:
            arr.append(temporary.val)
            temporary=temporary.next
        left-=1
        right-=1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        temporary=head
        i=0
        while temporary is not None:
            temporary.val=arr[i]
            temporary=temporary.next
            i=i+1
            
       
        return head
        