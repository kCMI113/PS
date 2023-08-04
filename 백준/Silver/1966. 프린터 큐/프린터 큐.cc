#include<iostream>
#include<queue>
#define cost first
#define pos second

using namespace std;

class printer_queue{
    private:
        int N, M;
        queue<pair<int, int>> docs; //(cost, pos)
        priority_queue<int> sorted_cost; //cost
    public:
        printer_queue(){cin>>N>>M;}
        ~printer_queue(){}
        void input(){
            int cost;

            for(int pos=0; pos < N; pos++){
                cin>>cost;
                sorted_cost.emplace(cost);
                docs.emplace(cost, pos);
            }
        }
        int find_query(){
            int cnt = 1;
            while(!sorted_cost.empty()){
                int max = sorted_cost.top();
                pair<int, int> now_docs = docs.front();
                docs.pop();

                if(now_docs.cost == max && now_docs.pos == M) {return cnt;}
                if(now_docs.cost == max) {cnt++; sorted_cost.pop();}
                else{docs.emplace(now_docs);}
            }
            return -1;
        }
};

int main(void){
    int n_Test, res;
    cin>>n_Test;

    for(int i=0; i<n_Test; i++){
        printer_queue pq;
        pq.input();
        res = pq.find_query();
        if(res > 0){cout<<res<<endl;}
        else{cout<<"wrong"<<endl;}

    }
    return 0;
}