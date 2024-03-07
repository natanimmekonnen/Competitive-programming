public class FindMissingandRepeatedValues {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int[] a = new int[2];
        int n = grid.length * grid.length;
        int[] arr = new int[n];
        int k = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                arr[k] = grid[i][j];
                k++;
            }
        }
        for (int i = 1; i <= n; i++) {
            int temp = -1;
            int l = i;
            for (int j = 0; j < arr.length; j++) {
                if (i == arr[j]) temp = i;
                if (l < n && arr[l] == arr[i-1]) {
                    a[0] = arr[l];
                }
                l++;
            }
            if(temp == -1) a[1] = i;
        }
        return a;

    }
}
