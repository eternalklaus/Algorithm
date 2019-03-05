#include "pch.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
 
using namespace std;
 
void initialize_colomnsum(int *colomnsum) {
    for (int i = 0; i < 100; i++) {
        colomnsum[i] = 0;
    }
}
 
int findmax_colomnsum(int *colomnsum) {
    int max = 0;
    for (int i = 0; i < 100; i++) {
        if (colomnsum[i] > max) {
            max = colomnsum[i];
        }
    }
    return max;
}
 
int findmax_4(int v1, int v2, int v3, int v4) {
    int max;
    max = v1;
    if (max < v2) {
        max = v2;
    }
    if (max < v3) {
        max = v3;
    }
    if (max < v4) {
        max = v4;
    }
    return max;
}
 
int main()
{
    int _;
    int arr[100][100];
    int colomnsum[100];
    int colomnsum_max;
    int widthsum;
    int max;
    int right_down;
    int left_down;
    int final_max;
 
    for (int n = 0; n < 10; n++) {
        cin >> _; // 쓸모없는거 테스트케이스 번호 입력
        // 초기화
        initialize_colomnsum(colomnsum);
        widthsum = 0;
        max = 0;
        right_down = 0;
        left_down = 0;
 
        for (int i = 0; i < 100; i++) {
            widthsum = 0;
            for (int j = 0; j < 100; j++) {
                cin >> arr[i][j];
                widthsum += arr[i][j]; // 1. 가로값 업데이트
                colomnsum[j] += arr[i][j]; // 2. 세로합값도 업데이트
                
                // 3. 대각선값 업데이트
                if (i == j) {
                    right_down += arr[i][j];
                }
                else if ((i + j) == 99) {
                    left_down += arr[i][j];
                }
            }
            // 가로100개 입력다받았당
            if (widthsum > max) {
                max = widthsum;
            }
 
        }
        // max, right_down, left_down, colomnsum[100] 이것중에서 최댓값을 구한다
        colomnsum_max = findmax_colomnsum(colomnsum);
 
        // max, right_down, left_down, colomnsum_max 이것중에서 최댓값을 구한다
        final_max = findmax_4(max, right_down, left_down, colomnsum_max);
 
        cout << "#" << (n + 1) << " ";
        cout << final_max << "\n";
    }
 
​
}