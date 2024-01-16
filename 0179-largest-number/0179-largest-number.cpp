#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        auto number_compare = [](int a, int b){
            // int -> str
            string str_a = to_string(a);
            string str_b = to_string(b);
            
            // compare
            return str_a + str_b > str_b + str_a;
        };
        
        sort(nums.begin(), nums.end(), number_compare);
        
        // if 0 is largest number
        if (nums[0] == 0){
            return "0";
        }
        
        // stringstream
        stringstream result;
        for (int num : nums){
            result << num;
        }
        // 이 문자열을 얻기 위한 함수 호출입니다.
        return result.str();
            
    }
};