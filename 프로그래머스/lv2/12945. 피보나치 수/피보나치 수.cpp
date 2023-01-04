#include <string>
#include <vector>
#define n_div 1234567

using namespace std;

// int fibo(int n){
    // if(n<=0) return 0;
    // if(n == 1) return 1;
    // return fibo(n-1)%n_div + fibo(n-2)%n_div;
// }

int solution(int n) {
    // int answer = fibo(n)%n_div;

    vector<int> fibo(n+1,0);
    fibo[1]=1;
    
    for(int i=2; i<=n; i++){
        fibo[i] = fibo[i-2]%n_div + fibo[i-1]%n_div;
    }
    
    int answer = fibo[n]%n_div;
    return answer;
}