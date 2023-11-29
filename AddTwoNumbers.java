public class AddTwoNumbers {
    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode() {}
     *     ListNode(int val) { this.val = val; }
     *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     * }
     */
    class Solution {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

            ListNode l3=new ListNode(0);
            ListNode head=l3;

            int carry=0;

            while(l1!=null||l2!=null)
            {int sum=carry;

                if(l1!=null)
                {
                    sum+=l1.val;
                    l1=l1.next;

                }
                if(l2!=null)
                {
                    sum+=l2.val;
                    l2=l2.next;

                }
                l3.next=new ListNode(sum%10);
                carry=sum/10;
                l3=l3.next;

            }
            if(carry>0)
            {
                l3.next=new ListNode(carry);
            }
            return head.next;


        }
    }
}
