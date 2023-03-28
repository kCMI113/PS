#include<bits/stdc++.h>
using namespace std;

int main(void){
    int n, store;
    vector<int> res = {0,0};
    cin>>n;

    for(int i=2; i<=n; i++){
		store = res[i-1] + 1;
        if(i%2 == 0) store = min(store,res[i/2]+1);
        if(i%3 == 0) store = min(store,res[i/3]+1);
        
        res.push_back(store);
    }
    cout<<res.back();
    
    return 0;
}