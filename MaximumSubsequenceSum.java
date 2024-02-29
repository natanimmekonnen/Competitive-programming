import java.util.Arrays;

public class MaximumSubsequenceSum {
public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int maxSum = maxSubsequenceSum(arr, arr.length);
        System.out.println("Maximum subarray sum: " + maxSum);
    }
}


    public static int maxSubsequenceSum(int[] arr, int n) {
        if (n == 1) {
            return arr[0];
        }

        int m = n / 2;
        int leftMaxSum = maxSubsequenceSum(arr, m);
        int rightMaxSum = maxSubsequenceSum(Arrays.copyOfRange(arr, m, n), n - m);

        int sum = 0;
        int leftSum = Integer.MIN_VALUE;
        int rightSum = Integer.MIN_VALUE;

        for (int i = m; i < n; i++) {
            sum += arr[i];
            rightSum = Math.max(rightSum, sum);
        }

        sum = 0;
        for (int i = m - 1; i >= 0; i--) {
            sum += arr[i];
            leftSum = Math.max(leftSum, sum);
        }

        int overallMax = Math.max(leftMaxSum, rightMaxSum);
        return Math.max(overallMax, leftSum + rightSum);
    }


}