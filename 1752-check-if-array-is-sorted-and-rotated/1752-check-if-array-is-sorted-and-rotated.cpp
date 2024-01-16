#include <vector>

class Solution {
public:
    bool check(std::vector<int>& nums) {
        int n = nums.size();
        int rotated_count = 0;

        // Count the number of rotations
        for (int i = 0; i < n - 1; ++i) {
            if (nums[i] > nums[i + 1]) {
                rotated_count++;
            }
        }

        // Handle the circular property
        if (nums[n - 1] > nums[0]) {
            rotated_count++;
        }

        // There should be at most one rotation for a sorted and rotated array
        return rotated_count <= 1;
    }
};
