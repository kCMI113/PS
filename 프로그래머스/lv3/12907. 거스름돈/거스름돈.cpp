#include <bits/stdc++.h>
#define MAX 100001

using namespace std;

int solution(int n, vector<int> money) {
    int answer=0, i=money[0];
    vector<int> dp(MAX);
    dp[0]=1;
    while(i<=n){
        dp[i] = 1;
        i += money[0];
    }
    for(int i=1; i<money.size(); i++){
        for(int j=0; j<=n; j++){
            if(j >= money[i]){
                dp[j] += dp[j-money[i]]%1000000007;
            }
        }
    }
    answer = dp[n];
    return answer;
}