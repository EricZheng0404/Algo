import java.util.Map;
import java.util.HashMap;
class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int res = 0;
        int cumulativeSum = 0;
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num:nums) {
            cumulativeSum += num;
            if (cumulativeSum == goal) {
                res += 1;
            }
            if (freq.containsKey(cumulativeSum - goal)){
                res += freq.get(cumulativeSum - goal);
            }
            freq.put(cumulativeSum, freq.getOrDefault(cumulativeSum, 0) + 1);
        }
        return res;
    }
}