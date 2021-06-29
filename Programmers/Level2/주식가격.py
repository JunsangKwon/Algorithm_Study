def solution(prices):
    answer = []
    for i in range(len(prices)):
        flag = False
        count = 0
        for j in range(i+1, len(prices)):
            if(prices[i] > prices[j]):
                count += 1
                answer.append(count)
                flag = True
                break
            else:
                count += 1
                continue
        if(not flag):
            answer.append(count)
                
                
    return answer