def solution(numbers):
    strings = list(map(str, numbers))
    strings.sort(key=lambda x: x*4, reverse=True)
    return str(int(''.join(strings)))
