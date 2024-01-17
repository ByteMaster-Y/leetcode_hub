#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        // 각 값의 발생 횟수를 저장하기 위한 unordered_map
        unordered_map<int, int> count_map;
        
        for (int num : arr){
            count_map[num]++;
        }
        
        unordered_set<int> occurrences;
        
        for (const auto& entry : count_map){
            if(!occurrences.insert(entry.second).second){
                // 여기서 entry.second는 unordered_map에서 추출한 발생 횟수 값이고, 
                // occurrences.insert(entry.second).second에서 
                // 첫 번째 second는 std::pair의 bool을 나타내며, 
                // 두 번째 second는 bool 값 자체를 나타냅니다.
                // 따라서 값을 삽입하고, 그 결과로 발생 횟수가 이미 존재하는지 여부를 
                // 나타내는 bool 값을 반환합니다.


                return false;
            }
        }
        return true;
        
    }
};