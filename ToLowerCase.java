public class ToLowerCase {
    public String toLowerCase(String s) {
        char[] smallLetter=s.toCharArray();
        String smalllet="";
        for(int i=0;i<smallLetter.length;i++)
        {

            int num=(int) smallLetter[i];
            if(num<91&&num>=65)
            {
                num+=+32;
                smallLetter[i]=(char)num;

            }
            smalllet+=smallLetter[i];



        }
        return smalllet;
    }
}
