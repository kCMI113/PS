#include<bits/stdc++.h>
using namespace std;

int main(void){
    int n,m,k,x;
    cin>>n>>m>>k>>x;

    vector<vector<int>> graph(n+1);
    vector<int> dpeth(n+1,-1);

    for(int i=0; i<m; i++){
        int a,b;
        cin>>a>>b;
        graph[a].push_back(b);
    }
    // bfs
    queue<int> Q;
    vector<int> res;
    Q.push(x);
    dpeth[x] = 0;

    while(!Q.empty()){
        int now = Q.front();
        Q.pop();
        for(auto node:graph[now]){
            if(dpeth[node]==-1){
                Q.push(node);
                dpeth[node] = dpeth[now] + 1;
                if(dpeth[node]== k) res.push_back(node);
            }
        }
    }
    
    bool check = false;
    for (int i = 1; i <= n; i++) {
        if (dpeth[i] == k) {
            cout << i << '\n';
            check = true;
        }
    }
    if (!check) cout << -1 << '\n';
}