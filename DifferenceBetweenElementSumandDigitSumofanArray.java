public class DifferenceBetweenElementSumandDigitSumofanArray {
    public int differenceOfSum(int[] nums) {
        int digit=0;
        int elem=0;
        for(int i=0;i<nums.length;i++)
        {
            elem+=nums[i];
            while(nums[i]>0)
            {
                digit+=nums[i]%10;
                nums[i]=nums[i]/10;

            }
        }
        return Math.abs(elem-digit);


    }
}
