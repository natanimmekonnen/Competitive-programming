public class NumberOfEmployeesWhoMetTheTarge {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {

        int meets=0;
        for (int i=0;i<hours.length;i++)
        {
            if(hours[i]>=target)
            {
                meets ++;
            }
        }
        return meets;
    }}
