def solution(numbers):
    answer = []
    sums = set()

    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            sums.add(numbers[i] + numbers[j])

    answer = list(sums)
    answer.sort()
