public class MaximumNumberofWordsFoundinSentences {
    public int mostWordsFound(String[] sentences) {
        int maxString=0;
        for(String wordCount: sentences)
        {
            int length=wordCount.split(" ").length;
            if(length>maxString)
            {
                maxString=length;
            }

        }
        return maxString;
    }
}
