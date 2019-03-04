#include <stdio.h>
#include <stdlib.h>
#include <iostream>
 
using namespace std;
 
void initialise_array(int *ret, int value) {
    for (int i = 5; i >= 0; i--) { // 최대 자릿수는 6
        if (value == 0) {
            ret[i] = -1;
            continue;
        }
        ret[i] = value % 10; // 123 -> {0,0,0,1,2,3}
        value = value / 10;
    }
}
 
void swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
 
int find_i_start(int *ret) {
    for (int i = 0; i <= 5; i++) {
        if (ret[i] != -1) {
            return i;
        }
    }
}
 
int isthere_any_duplicate(int i_start, int* ret) {
    for (int i = i_start; i <= 5; i++) {
        for (int j = i; j <= 5; j++) {
            if (i != j) {
                if (ret[i] == ret[j]) {
                    return 1;
                }
            }
        }
    }
    return 0;
}
 
void printret(int *ret) {
    for (int j = 0; j <= 5; j++) {
        if (ret[j] == -1) continue;
        printf("%d", ret[j]);
    }
}
 
void sort_gogo(int *ret, int changenum) {
    int max, min;
    int i_max, i_min;
    int max_count = 0;
    int i_start = find_i_start(ret);
    int duplicated_flag = 0;
    int scan_right;
    int scan_left;
 
    while (changenum > 0) {
        // 시작대상 i_start 를 구한다. 앞에서부터 스캔하면서 정렬이 안된 인덱스를 리턴한다. 
        i_start = find_i_start(ret);
 
        // 오른쪽부터 돌면서 가장큰값의 idx 구하기
        scan_right = 5;
        scan_left = i_start;
        while (1) {
            scan_right = 5;
            max = ret[scan_right];
            i_max = scan_right;
 
            // 자 이제 가장 큰 값과 그 인덱스를 찾는다
            while (scan_right >= scan_left) { // 5부터 시작해서 왼쪽으로 간당
                if (max < ret[scan_right]) {
                    max = ret[scan_right];
                    i_max = scan_right;
                    max_count = 1;
                }
                else if (max == ret[scan_right]) {
                    max_count++;
                }
                scan_right--; // 4, 3, 2... 이렇게 줄입니다
            }
 
            // 탈출조건을 설정한다. 가장큰 i가 맨왼쪽 i와 동일인물이 아니라면 탈출가능!
            if (i_max != scan_left) { 
                break;
            }
            scan_left++;
        }
 
        /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
        if ((scan_left == 6) && (i_max == 5)) { // 이거슨 완벽한 상태라는 방증이다. 
            break;
        }
        /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
 
 
        // 왼쪽부터 돌면서 가장작은값의 idx구하기
        max_count = max_count < changenum ? max_count : changenum; // 두개중 더작은걸 골라서,
        min = ret[i_start];
        i_min = i_start;
        for (int i = i_start; i < 6; i++) {
            if (max_count == 0) break;
            if (max < ret[i]) continue; // 만약에 맨앞에있는 값이 더큰 값이라면... 음...(모르는척)
 
            if (ret[i] < min) { // 더 작은얘의 발견
                min = ret[i];
                i_min = i;
            }
            max_count--;
        }
        swap(&ret[i_min], &ret[i_max]);
        changenum--;
    }
 
    duplicated_flag = isthere_any_duplicate(i_start, ret);
    if (changenum > 0) {
        if (duplicated_flag == 1) {
            // 아무 것도 하지 않는다.
        }
        else if (changenum % 2 == 0) {
            // 아무 것도 하지 않는다.
        }
        else if (changenum % 2 == 1) {
            swap(&ret[4], &ret[5]);
        }
        
    }
 
}
 
 
int main()
{
    int n;
    int value;
    int changenum;
    int ret[6];
    int len;
    scanf("%d", &n);
 
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &value, &changenum);
        printf("#%d ", i + 1);
        initialise_array(ret, value);
        sort_gogo(ret, changenum);
 
        printret(ret);
        printf("\n");
    }
}