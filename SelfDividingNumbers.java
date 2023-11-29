public class SelfDividingNumbers {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> out = new ArrayList<>();
        for(int i=left;i<=right;i++)
        {

            if(check(i))
            {
                out.add(i);

            }

        }
        return  out;
    }
    public boolean check(int number)
    {
        int digits=0,count=0,hold,number1=number, originalNumber=number;

        if(number==0)
        {
            return false;
        }


        while(number>0)
        {
            number /=10;

            digits++;

        }

        for(int i=1;i<=digits;i++)
        {
            hold=number1%10;

            if(hold!=0) {

                if (originalNumber % hold == 0) {
                    number1 /= 10;
                    count++;

                }
            }
        }

        if(count==digits)
        {
            return true;
        }

        return false;


    }
}
