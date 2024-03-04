import java.util.HashSet;

public class JewelsandStones {
    public int numJewelsInStones(String jewels, String stones) {
        char[] word= jewels.toCharArray();
        HashSet<Character> ha=new HashSet<Character>();
        int count=0;
        char[] words=stones.toCharArray();

        for(int i=0;i<word.length;i++)
        {
            ha.add(word[i]);

        }
        for(int i=0;i<words.length;i++)
        {
            if(ha.contains(words[i]))
                count++;
        }

        return  count;
    }
}
