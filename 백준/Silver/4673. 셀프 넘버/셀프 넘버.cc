#include<iostream>
using namespace std;

int d(int n){
    int res;
    res = n+n%10;
    n=n/10;
    while(n>0) {
        res = res+n%10;
        n = n/10;
    }
    return res;
};

int main(void){

    int* arr = new int[10000];

    for(int i=0; i<10000; i++){
        if(d(i+1)<=10000) arr[d(i+1)-1] = -1;
    }
    for(int i=0; i<10000; i++){
        if(arr[i] != -1) cout<<i+1<<endl;
    }

    delete[] arr;

    return 0;
}
