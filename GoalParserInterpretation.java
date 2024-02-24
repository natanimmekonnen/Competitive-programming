public class GoalParserInterpretation {
    public String interpret(String command) {
        char[] array=command.toCharArray();
        StringBuilder word= new StringBuilder();
        for(int i=0;i<array.length;i++)
        {
            if(array[i]=='G')
            {
                word.append('G');
            }
            else if(array[i]=='('&&array[i+1]=='a')
            {
                word.append('a');
                word.append('l');
            }
            else if(array[i]=='('&&array[i+1]==')')
            {
                word.append('o');
            }

        }
        return word.toString();

    }
}
