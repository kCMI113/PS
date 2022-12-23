#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;

int main(void){
    int a,b,temp;
    cin>>a>>b;
    bool arr[b+1];
    memset(arr, false, sizeof(arr));

    arr[1] = true;
    temp = 2;

    while(temp <= sqrt(b)){
        if(arr[temp]== false){
            for(int i=2; temp*i <= b; i++) {
                arr[temp*i] = true;
            }
        }
        temp++;
    }

    for(int i=a; i<=b; i++){
       if(arr[i] == false) cout<<i<<"\n";
    }

    return 0;
}