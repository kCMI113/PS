#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> nums;
    int idx_pre=0, idx_next;    
    
    while(1){
        idx_next = s.find(" ", idx_pre);
        if(idx_next == string::npos){
            nums.push_back(stoi(s.substr(idx_pre,s.size()-idx_pre)));
            break;
        }
        nums.push_back(stoi(s.substr(idx_pre,idx_next-idx_pre)));
        idx_pre = idx_next+1;
    }
    answer += to_string(*min_element(nums.begin(), nums.end())) 
            +" "+ to_string(*max_element(nums.begin(), nums.end()));          
    return answer;
}