def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        impossible = False
        isLearned = [False]*27
        for i in range(len(skill_tree)):
            if(skill_tree[i] in skill):
                index = skill.index(skill_tree[i])
                print(index)
                isLearned[index] = True
                for k in range(0, index+1):
                    if(not isLearned[k]):
                        impossible = True
                        break
            else:
                continue
        if(not impossible):
            answer += 1
        else:
            impossible = False

    return answer
