def solution(n):
    answer = 0
    for i in range(1, n+1):
        seq_sum = 0
        for j in range(i, n+1):
            seq_sum += j
            if(seq_sum == n):
                answer += 1
                break
            elif(seq_sum > n):
                break

    return answer
