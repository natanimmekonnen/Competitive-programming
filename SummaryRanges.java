import java.util.List;
import java.util.ArrayList;

public class SummaryRanges {
    public List<String> summaryRanges(int[] nums) {
        List<String> answer=new ArrayList<>();
        for(int i=0;i<nums.length;i++)
        {
            int num=nums[i];
            while(i+1<nums.length&&nums[i+1]==nums[i]+1)
            {
                i++;

            }
            if(num==nums[i])
            {
                answer.add(String.valueOf(num));
            }
            else
            {
                answer.add(num+"->"+ nums[i]);
            }


        }
        return answer;

    }

}
