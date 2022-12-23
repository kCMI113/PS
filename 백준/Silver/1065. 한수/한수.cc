#include<iostream>
using namespace std;

int hansu(int n){

    if(n < 100) return 1;

    int i,d;
    int* arr = new int[4];

    i=0;
    while(n > 0){
        arr[i] = n%10;
        i++;
        n=n/10;
    }

    d=arr[i-1]-arr[i-2];


    for(int j=i-1; j>0; j--){
        if(arr[j]-arr[j-1] != d) return 0;
    }

    return 1;
};

int main(void){

    int n, cnt;
    cin>>n;

    cnt=0;
    for(int i=1; i<n+1; i++) {
        cnt = cnt+hansu(i);
    }

    cout<<cnt<<endl;

    return 0;
}