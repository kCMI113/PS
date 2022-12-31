#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int tot = brown + yellow;
    int row, col;
    for(row=1; row<=tot/2; row++){
        col = brown/2-row+2;
        if((brown/2 == row+col-2) && (yellow == (row-2)*(col-2))){
            answer.push_back(col);
            answer.push_back(row); 
            break;
        }
    }
    return answer;
}