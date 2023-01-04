#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<int> InOut;
    
    if(s.front() == ')' || s.back() == '(') answer = false;
    else{
        for(auto c:s){
            if(c == '(')            InOut.push(1);
            else if(!InOut.empty()) InOut.pop();
        }
        answer = InOut.empty();
    }
    return answer;
}