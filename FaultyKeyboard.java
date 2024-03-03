import java.util.ArrayList;
import java.util.Collections;

public class FaultyKeyboard {
    public String finalString(String s) {
        char[] word=s.toCharArray();
        ArrayList<Character> tobe=new ArrayList<Character>();
        for( int i=0;i<word.length;i++)
        {
            if(word[i]=='i')
            {
                Collections.reverse(tobe);
            }
            else
            {
                tobe.add(word[i]);
            }
        }

        return tobe.toString().replaceAll("[,\\s\\[\\]]", "");

    }
}
