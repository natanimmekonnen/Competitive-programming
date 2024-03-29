import java.util.Arrays;

public class MaxNumberofKSumPairs {
    public int maxOperations(int[] nums, int k) {
        int left=0;
        int right=nums.length-1;
        Arrays.sort(nums);
        int operation=0;
        while(left<right)
        {
            if(nums[left]+nums[right]==k)
            {
                operation++;
                left++;
                right--;

            }
            else if(nums[left]+nums[right]<k)
            {
                left++;
            }
            else
            {
                right--;
            }


        }
        return operation;
    }
}
