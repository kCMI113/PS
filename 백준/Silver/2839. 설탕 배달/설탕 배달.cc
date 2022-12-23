#include<iostream>
using namespace std;

int main(void){
    int n,f,t;

    cin>>n;
    f = n/5;

    if((n-5*f)%3 == 0) t=(n-5*f)/3;
    else{
        for(int i=0; f>0; i++){
            f=f-1;
            if((n-5*f)%3 == 0) {
                t=(n-5*f)/3;
                break;
            }
        }
        if(n%3 != 0&&f==0){
            f=-1;
            t=0;
        }
    }
    cout << f+t<<endl;

    return 0;
}