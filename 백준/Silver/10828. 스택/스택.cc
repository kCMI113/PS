#include<iostream>
#include<string>
using namespace std;

class mystack{
private:
    int n,cnt;
    int* arr;
public:
    mystack(int a){
        n=a;
        arr=new int[n+1]{-1,};
        cnt=0;
        }
    void push(int x){arr[cnt]=x; cnt++;}
    int size(){
        int i=0;
        while(arr[i]>0) i++;
        return i;
    }
    int empty(){
        if(size() == 0){
            cnt=0;
            return 1;
        }else return 0;
    }
    int top(){
        if(empty() == 1) return -1;
        else return arr[size()-1];
    }
    int pop(){
        int temp;
        if(empty() ==1 ) return -1;
        else{
            temp = top();
            arr[size()-1] = -1;
            cnt--;
            return temp;
        }
    }
};
int main(void){
    int n1;
    cin>>n1;
    string str;
    mystack S(n1);

    for(int i=0; i<n1; i++){
        cin>>str;
        if(str == "push"){
            int a;
            cin>>a;
            S.push(a);
        }
         else if(str == "pop") cout<< S.pop()<<"\n";
         else if(str == "size") cout<< S.size()<<"\n";
         else if(str == "empty") cout<< S.empty()<<"\n";
         else if(str == "top") cout<< S.top()<<"\n";
    }
    return 0;
}