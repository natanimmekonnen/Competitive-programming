public class ConcatenationofArray {
    public int[] getConcatenation(int[] nums) {
        int j=nums.length;
        int[] arr=new int[2*j];
        for(int i=0;i<j;i++)
        {
            arr[i]=nums[i];
            System.out.println(j);
            arr[i+j]=nums[i];

        }
        return arr;

    }
}
