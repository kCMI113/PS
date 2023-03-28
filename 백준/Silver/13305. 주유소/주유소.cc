#include<bits/stdc++.h>
using namespace std;

int main(void){
    int n, tot_cost=0, min_cost, temp;
    vector<int> km, cost;
    cin>>n;

    for(int i=0; i<n-1; i++){
		cin>>temp;
    	km.push_back(temp);
    }
	for(int i=0; i<n; i++){
		cin>>temp;
    	cost.push_back(temp);
    }
    min_cost = cost.front();

    for(int i=0; i<n-1; i++){
        min_cost = min(min_cost,cost[i]);
        tot_cost += min_cost*km[i];
    }
    cout<<tot_cost;

    return 0;
}
