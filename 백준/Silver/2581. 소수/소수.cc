#include<iostream>
using namespace std;

int isPrime(int n){

    if(n==1) return 0;
    else if(n==2 || n==3 ) return 1;
    else{
        if(n%2 == 0) return 0;
        else if(n%3 == 0) return 0;
        else{
            for(int i=5; i<n-1; i++){
                if(n%i == 0) return 0;
            }
        }
    }
    return 1;
};

int main(void){
    int a,b,sum,min;

    cin>>a>>b;
    sum=0;
    min=b;

    for(int i=a; i<b+1; i++){
        if(isPrime(i)==1){
            sum=sum+i;
            if(i < min) min = i;
        }
    }

    if(sum==0)  cout<<"-1"<<endl;
    else    cout<<sum<<endl<<min<<endl;

    return 0;
}