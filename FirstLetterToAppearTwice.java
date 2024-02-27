import java.util.HashSet;

public class FirstLetterToAppearTwice {
    public char repeatedCharacter(String s) {
        HashSet<Character> chara = new HashSet<Character>();
        char[] word=s.toCharArray();
        for(int i=0;i<word.length;i++)
        {
            if(chara.contains(word[i]))
            {
                return word[i];
            }
            chara.add(word[i]);
        }
        return 'a';
    }
}
