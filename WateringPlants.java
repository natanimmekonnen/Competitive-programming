public class WateringPlants {
    public int wateringPlants(int[] plants, int capacity) {
        int n = plants.length;
        int steps = 0;
        int currCapacity = 0;

        for (int i = 0; i < n; i++) {
            if (currCapacity + plants[i] <= capacity) {
                currCapacity += plants[i];
            } else {
                steps += i * 2;
                currCapacity = plants[i];
            }
        }

        return steps + n;
    }
}
