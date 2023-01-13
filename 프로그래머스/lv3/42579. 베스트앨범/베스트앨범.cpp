#include <bits/stdc++.h>
#define pairs pair<int,int>
#define sipair pair<string, int>
using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string, vector<pairs>> Total;
    map<string, int> rank;
    
    for(int i=0; i<plays.size(); i++){
        Total[genres[i]].push_back({plays[i], i});
        rank[genres[i]] += plays[i];
    }
    vector<sipair> rankV(rank.begin(), rank.end());
    sort(rankV.begin(), rankV.end(), [](const sipair a, const sipair b){return a.second > b. second;});
    
    for(auto R:rankV){
        if(Total[R.first].size()<2) answer.push_back(Total[R.first][0].second);
        else{
            sort(Total[R.first].begin(), Total[R.first].end(), [](const pairs a, const pairs b){
                if(a.first==b.first) return a.second < b.second;
                else return a.first > b.first;});
            answer.push_back(Total[R.first][0].second);
            answer.push_back(Total[R.first][1].second);
        }
    }
    
    return answer;
}