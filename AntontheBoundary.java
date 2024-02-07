public class AntontheBoundary {

        public int returnToBoundaryCount(int[] nums) {
            int sum=0,blink=0;
            for(int i=0;i<nums.length;i++)
            {
                sum+=nums[i];
                if(sum==0)
                {
                    blink++;
                }
            }

            return blink;





    }
}
