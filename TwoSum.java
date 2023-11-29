public class TwoSum {
    public int[] twoSum(int[] numbers, int target) {
        int index1=0,index2=0;
        int left=0,right=numbers.length-1;
        int[] arr=new int[2];

        while(left<right)
        {
            int sum=numbers[left]+numbers[right];
            if(sum==target)
            {
                index1=left;
                index2=right;
                break;
            } else if (sum<target) {
                left++;


            }
            else {
                right--;
            }
        }

        arr[0]=index1+1;
        arr[1]=index2+1;
        return arr;


    }
}
