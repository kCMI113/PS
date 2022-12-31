#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    int row = arr1.size();
    int col = arr1.begin()->size();
    answer.resize(row, vector<int>(col));
    
    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            answer[i][j] = arr1[i][j]+arr2[i][j];
        }
    }
    return answer;
}