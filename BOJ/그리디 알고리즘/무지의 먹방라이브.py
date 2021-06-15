def solution(food_times, k):
    answer = 0
    if(sum(food_times) < k):
        return -1
    for i in range(k+1):
        if(food_times[answer] == 0):
            while(food_times[answer] == 0):
                answer = (answer+1) % len(food_times)
        if i==k:
            return answer+1
        food_times[answer] -= 1
        answer = (answer+1) % len(food_times)
