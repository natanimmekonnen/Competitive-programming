public class DivisibleandNonDivisibleSumsDifference {
    public int differenceOfSums(int n, int m) {
        int num1=0,num2=0;
        for(int i=1;i<=n;i++)
        {
            if(i%m==0)
            {
                num2+=i;
            }
            if(i%m!=0)
            {
                num1+=i;

            }
        }
        System.out.println(num1);
        System.out.println(num2);
        return num1 - num2;
    }
}
