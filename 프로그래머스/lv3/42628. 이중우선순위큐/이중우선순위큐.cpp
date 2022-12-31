#include <string>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer = {0,0};
    deque<int> que;
    string com;
    int data;
    
    for(auto op:operations){
        com = op.substr(0,1);
        data = stoi(op.substr(2,op.length()-2));
        
        if(com =="I") que.push_back(data);
        else if(!que.empty() && data == -1) que.pop_front();
        else if(!que.empty() && data == 1)  que.pop_back();
        sort(que.begin(), que.end());
    }
    if(!que.empty()){ answer[0] = que.back(); answer[1] = que.front(); }
    return answer;
}