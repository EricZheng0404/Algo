class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int na = nums1.length;
        int nb = nums2.length;
        int n = na + nb;
        // When we have odd number of elements
        if (n % 2 == 1) {
            return solve(nums1, nums2, n / 2,  0, na - 1, 0, nb - 1);
        // When we have even number of elements
        } else {
            return (solve(nums1, nums2, n / 2 - 1, 0, na - 1, 0, nb - 1) + 
            solve(nums1, nums2, n / 2, 0, na - 1, 0, nb - 1)) / 2;
        }
    }

    // k represents the kth element we wanted (0-index)
    private double solve(int[] nums1, int[] nums2, int k, int aStart, int aEnd, int bStart, int bEnd) {
        // Base case: If one array is all passed, then we need to find the index in the other array
        if (aStart > aEnd) {
            return (double) nums2[k - aStart];
        }
        if (bStart > bEnd) {
            return (double) nums1[k - bStart];
        }
        int aMid = (aStart + aEnd) / 2, bMid = (bStart + bEnd) / 2;
        int aValue = nums1[aMid], bValue = nums2[bMid];
        // If the k is in the right half, then we can get rid of the smaller left half
        if (aMid + bMid < k) {
            if (aValue < bValue) {
                return solve(nums1, nums2, k, aMid + 1, aEnd, bStart, bEnd);
            } else {
                return solve(nums1, nums2, k, aStart, aEnd, bStart + 1, bEnd);
            }
        // The k is in the left half, then we can get rid of the larger right half
        } else {
            if (aValue < bValue) {
                return solve(nums1, nums2, k, aStart, aEnd, bStart, bMid - 1);
            } else {
                return solve(nums1, nums2, k, aStart, aMid - 1, bStart, bEnd);
            }
        }
    }
}