#include <vector>

class Solution {
public:
    bool check(std::vector<int>& nums) {
        int n = nums.size();
        int rotated_count = 0;
        
        for (int i = 0; i < n - 1; ++i){
            if (nums[i] > nums[i+1]){
                rotated_count++;
            }
        }
        
         
        if (nums[n - 1] > nums[0]){
            rotated_count++;
        }

        return rotated_count<=1;
    }
};
