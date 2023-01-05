#include <string>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer = {0,0};
    map<string, int> list;
    int i=0;
    char pre = (words.front()).front();
    
    for(auto W:words){
        auto res = list.insert({W,i%n});
        if(res.second == false || pre != W.front()) {
            answer[0] = i%n+1;
            answer[1] = i/n+1;
            break;
        }
        pre = W.back();
        i++;

    }
    return answer;
}