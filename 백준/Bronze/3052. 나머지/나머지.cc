#include<iostream>
#include<set>
using namespace std;

int main(void){
    int n=10;
    set<int> mod;

    for(int i=0; i<n; i++){
        int temp;
        cin>>temp;
        mod.insert(temp%42);
    }
    cout<<mod.size()<<endl;

    return 0;
}