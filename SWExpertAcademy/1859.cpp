#include <stdio.h>
#include <stdlib.h>
#include <iostream>
 
long long calculatesum(int* prices, int days) {
    long long sum = 0;
    int max = 0;
    int j;
    // 뒤부터 순회하면서 최대값 업데이트
    for (int i = 0; i < days; i++) {
        j = days - i - 1;
        if (prices[j] > max) {
            max = prices[j]; // 최대값 갱신
        }
        else { // 미래에 더큰 최대값이 이따 ㅜㅜ 
            sum = sum + max - prices[j];
        }
    }
    return sum;
}
int main()
{
    int n, days;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &days);
        int *prices = new int [days];
 
 
        for (int j = 0; j < days; j++) {
            scanf("%d", &prices[j]); // 가격 입력
        }
 
        // 출력 부분
        printf("#%d ", i+1);
 
        long long sum = calculatesum(prices, days);
        printf("%lld\n", sum);
        free(prices);
    }   
}