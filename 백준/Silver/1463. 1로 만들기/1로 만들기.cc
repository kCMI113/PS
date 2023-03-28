#include<bits/stdc++.h>
using namespace std;

int main(void){
    int n;
    vector<int> res = {0,0};
    cin>>n;

    for(int i=2; i<=n; i++){
        vector<int> store = {res[i-1] + 1};
        if(i%2 == 0) store.push_back(res[i/2]+1);
        if(i%3 == 0) store.push_back(res[i/3]+1);
        res.push_back(*min_element(store.begin(),store.end()));
    }
    cout<<res.back();
    return 0;
}