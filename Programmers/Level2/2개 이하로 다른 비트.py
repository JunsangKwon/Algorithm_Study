# 통과 코드
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        b_value = bin(numbers[i])[2:]
        if b_value[-1] == '0':
            answer.append(numbers[i] + 1)
        else:
            r_value = b_value[::-1]
            count = 0
            for j in range(len(r_value)):
                if r_value[j] == '1':
                    count += 1
                else:
                    break
            
            answer.append(numbers[i] + 2 ** (count - 1))
            
            
    return answer

# 마지막 테케 2개 시간초과 코드 
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        b_value = bin(numbers[i])[2:]
        
        index = 1
        while True:
            count = 0
            b_length = len(b_value)
            candidate_value = bin(numbers[i] + index)[2:]
            candidate_length = len(candidate_value)
            distance = candidate_length - b_length
            for _ in range(distance):
                b_value = '0' + b_value
            
            for j in range(candidate_length):
                if b_value[j] != candidate_value[j]:
                    count += 1
            
            if count <= 2:
                answer.append(numbers[i] + index)
                break
            index += 1
            
    return answer