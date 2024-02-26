public class GoatLatin {
    public String toGoatLatin(String sentence) {
        String[] words = sentence.split(" ");
        StringBuilder sent=new StringBuilder();
        for(int i=0;i<words.length;i++)
        {
            char[] each= words[i].toCharArray();

            if(each[0]=='a'||each[0]=='A'||each[0]=='e'||each[0]=='E'||each[0]=='i'||each[0]=='I'||each[0]=='o'||each[0]=='O'||each[0]=='u'||each[0]=='U')
            {
                sent.append(words[i]);
                sent.append("ma");

                for(int j=0;j<=i;j++)
                {
                    sent.append("a");
                }
                if(i!= words.length-1)
                    sent.append(" ");


            }
            else
            {
                sent.append(words[i].substring(1));
                sent.append(each[0]);
                sent.append("ma");
                for(int j=0;j<=i;j++)
                {
                    sent.append("a");
                }
                if(i!= words.length-1)
                    sent.append(" ");
            }
        }
        return sent.toString();

    }
}
