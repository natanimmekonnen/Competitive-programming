import java.util.HashMap;
import java.util.Map;

public class CountElementWithMaximumFrequency {
    public int maxFrequencyElements(int[] nums) {

        Map<Integer, Integer> map = new HashMap<>();
        int max = 0;
        int result = 0;
        for (int e : nums) {
            map.put(e, map.getOrDefault(e, 0) + 1);
            max = Math.max(max, map.get(e));

        }
        for (var e : map.entrySet()) {
            int current = e.getValue();
            if (current == max) {
                result++;
            }
        }
        return result * max;
    }
}
