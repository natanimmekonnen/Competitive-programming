public class SearchInRotatedSortedArray {
    public int search(int[] nums, int target) {
        int count=0;

        for(int num:nums)
        {
            count++;


            if(num==target)
            {

                return count-1;

            }

        }
        return -1;


    }
}
