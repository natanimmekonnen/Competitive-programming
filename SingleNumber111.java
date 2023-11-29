import java.util.HashSet;
import java.util.Iterator;
public class SingleNumber111 {
    public int[] singleNumber(int[] nums) {
        HashSet<Integer> seen=new HashSet<>();
        HashSet<Integer> duplicate=new HashSet<>();
        int[] arr=new int[2];
        for(int num:nums)
        {
            if(seen.contains(num))
            {
                duplicate.add(num);
            }
            else
            {
                seen.add(num);
            }
        }

        seen.removeAll(duplicate);
        Iterator<Integer> iter=seen.iterator();
        arr[0]=iter.next();

        if(iter.hasNext()) {
            arr[1] = iter.next();
        }
        return arr;

    }
}
