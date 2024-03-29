public class CheckIfArrayIsSorted {
    boolean arraySortedOrNot(int[] arr, int n) {
        // code here
        int left=0;
        int right=1;
        while(right<n)
        {
            if(arr[left]>arr[right])
            {
                return false;
            }
            left++;
            right++;
        }
        return true;

    }
}
