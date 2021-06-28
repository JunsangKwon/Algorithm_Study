def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        newarray = array[commands[i][0]-1: commands[i][1]]
        newarray.sort()
        answer.append(newarray[commands[i][2]-1])

    return answer
