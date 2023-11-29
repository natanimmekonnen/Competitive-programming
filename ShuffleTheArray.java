public class ShuffleTheArray {
    public int[] shuffle(int[] nums, int n) {
        int[] array1 = Arrays.copyOfRange(nums, 0, n);
        int[] array2 = Arrays.copyOfRange(nums, n, nums.length);
        List<Integer> newArray= new ArrayList<>();
        int[] shuffledArray=new int[nums.length];

        for(int i=0;i<n;i++)
        {
            newArray.add(array1[i]);
            newArray.add(array2[i]);
        }
        for(int i=0;i<shuffledArray.length;i++)
        {
            shuffledArray[i]=newArray.get(i);
        }



        return shuffledArray;

    }
}
