from sys import stdin
import math

input = stdin.readline

n = int(input())

# 처음엔 모든 수가 소수인 것으로 초기화(0과 1은 제외)
arr = [True] * (n+1)
count = 0

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인
for i in range(2, int(math.sqrt(n)) + 1):
    # i가 소수인 경우(남은 수인 경우)
    if arr[i] == True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if arr[i]:
        count += 1

print(count)
