def solution(cacheSize, cities):
    answer = 0
    cache = []
    dictionary = {}
    if cacheSize == 0:
        return len(cities) * 5

    for i in range(len(cities)):
        if cities[i].lower() in cache:
            dictionary[cities[i].lower()] = i
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(cities[i].lower())
                dictionary[cities[i].lower()] = i
                answer += 5
            else:
                min_index = min(list(dictionary.values()))
                for j in range(len(cache)):
                    if dictionary[cache[j]] == min_index:
                        del dictionary[cache[j]]
                        del cache[j]
                        break
                cache.append(cities[i].lower())
                dictionary[cities[i].lower()] = i
                answer += 5

    return answer
