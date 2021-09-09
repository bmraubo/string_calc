def Add(string):
    if string == "":
        return 0
    else:
        answer = 0
        for num in string.split(','):
            answer += int(num)
        return answer 