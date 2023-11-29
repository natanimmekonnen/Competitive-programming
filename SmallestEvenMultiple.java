public class SmallestEvenMultiple {
    public int smallestEvenMultiple(int n) {
        int bigger=Math.max(n,2);

        while(true)
        {
            if(bigger%n==0 &&bigger%2==0)
            {
                return bigger;

            }

            ++bigger;
        }

    }}
