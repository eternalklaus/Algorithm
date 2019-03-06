#include "pch.h"
#include <iostream>
#include <set>
 
using namespace std;
 
set<int> s;
 
 
 
int findDFS(int generating, int leftnum, int arr[][4], int i, int j) { // generating : 현재 연성하고 있는 숫자. 
    int ret;
    
    if (leftnum == 0) {
        s.insert(generating);
        return generating;
    }
 
    //right
    if (j != 3) { // 오른쪽에 갈 공간이 있다면
        ret = arr[i][j + 1] + (10 * generating);
        findDFS(ret, leftnum - 1, arr, i, j + 1); // 남은수 업데이트, 오른쪽으로 한칸 이동
    }
 
    //left
    if (j != 0) {
        ret = arr[i][j - 1] + (10 * generating);
        findDFS(ret, leftnum-1, arr, i, j - 1); // 남은수 업데이트, 왼쪽으로 한칸 이동
    }
 
    //up
    if (i != 0) {
        ret = arr[i - 1][j] + (10 * generating);
        findDFS(ret, leftnum - 1, arr, i - 1, j); // 남은수 업데이트, 위로 한칸 이동
    }
 
    //down
    if (i != 3) {
        ret = arr[i + 1][j] + (10 * generating);
        findDFS(ret, leftnum - 1, arr, i + 1, j); // 남은수 업데이트, 아래로 한칸 이동
    }
}
 
 
 
int main() {
    int T;
    int arr[4][4];
 
 
    cin >> T;
 
    for (int _ = 0; _ < T; _++) {
        s.clear();
        
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> arr[i][j];
            }
        }
 
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                findDFS(0, 7, arr, i, j);
            }
        }
        cout << "#" <<(_+1)<<" "<< s.size() << "\n";
    }
}