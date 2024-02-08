public class NumberofSegmentsinaString {
    public int countSegments(String s) {
        String[] words=s.split(" ");
        int counyer=0;
        for(String st:words)
        {
            if(!st.isEmpty())
            {
                counyer++;
            }
        }
        return counyer;
    }
}
