#include <string>
#include <vector>

using namespace std;

int solution(vector<int> ingredient) {
    int answer = 0;
    vector<int> burger ={1,2,3,1};
    vector<int> check(4);
    for(int i=0; i+4<=ingredient.size(); i++){
        copy(ingredient.begin()+i,ingredient.begin()+i+4, check.begin());
        if(check==burger) {
            answer++;
            ingredient.erase(ingredient.begin()+i,ingredient.begin()+i+4);
            i-=4;
        }
    }
    return answer;
}