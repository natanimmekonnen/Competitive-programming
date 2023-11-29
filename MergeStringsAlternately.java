public class MergeStringsAlternately {
    public String mergeAlternately(String word1, String word2) {
        int num=Math.min(word1.length(), word2.length());;
        StringBuilder str=new StringBuilder();
        for(int i=0;i<num;i++)
        {

            str.append(word1.charAt(i));
            str.append(word2.charAt(i));

        }
        boolean isCheck=word1.length()>word2.length();
        if(isCheck)
        {
            str.append(word1.substring(word2.length()));
        }
        else
        {

            str.append(word2.substring(word1.length()));

        }
        return str.toString();
    }}
