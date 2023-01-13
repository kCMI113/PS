#include <bits/stdc++.h>
using namespace std;

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    int idx = n;
    sort(strings.begin(), strings.end(),[&idx](const string a, const string b){
        if(a[idx] == b[idx]) return a < b;
        else return a[idx] < b[idx];
        } );
    answer = strings;
    
    return answer;
}