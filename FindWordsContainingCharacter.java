import java.util.ArrayList;
import java.util.List;

public class FindWordsContainingCharacter {
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> numbers=new ArrayList<Integer>();
        for(int i=0;i< words.length;i++)
        {
            char[] word=words[i].toCharArray();
            for(char c:word)
            {
                if(c==x)
                {
                    numbers.add(i);
                    break;
                }

            }
        }
        return numbers;

    }
}
