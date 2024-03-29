#백준 1463: 1로 만들기

n = int(input())

# 각 정수마다 필요한 연산 횟수를 저장할 리스트 생성
dp = [0] * (n + 1)

# 2부터 n까지 순회하며 최소 연산 횟수 계산
for i in range(2, n + 1):
    # 현재 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 현재 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 현재 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# 정수 N을 1로 만들기 위한 최소 연산 횟수 출력
print(dp[n])



