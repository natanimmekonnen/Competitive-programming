
    import java.util.*;

    public class MergeTwoArrays {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int[] arr1 = new int[n];
            int[] arr2 = new int[m];

            for (int i = 0; i < n; i++) {
                arr1[i] = scanner.nextInt();
            }

            for (int i = 0; i < m; i++) {
                arr2[i] = scanner.nextInt();
            }

            int[] mergedArray = new int[n + m];
            int i = 0, j = 0, k = 0;

            while (i < n && j < m) {
                if (arr1[i] <= arr2[j]) {
                    mergedArray[k++] = arr1[i++];
                } else {
                    mergedArray[k++] = arr2[j++];
                }
            }

            while (i < n) {
                mergedArray[k++] = arr1[i++];
            }

            while (j < m) {
                mergedArray[k++] = arr2[j++];
            }
            
            for (int num : mergedArray) {
                System.out.print(num + " ");
            }
        }
    }


