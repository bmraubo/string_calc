def Add(string):
    def Empty(string):
        if string == "":
            return True
    if Empty(string):
        return 0
    else:
        if string[:2] == '//':
            if string.count('\n') > 1:
                if Empty(string[4:]):
                    return 0
                else:
                    answer = 0
                    for num in string[4:].split('\n'):
                        answer += int(num)
                    return answer
            elif Empty(string.split('\n')[1]):
                return 0
            else:
                answer = 0
                delimiter = string.split('\n')[0].strip('//')
                for num in string.split('\n')[1].split(delimiter):
                    answer += int(num)
                return answer
        else:
            answer = 0
            for num in string.replace('\n',',').split(','):
                answer += int(num)
            return answer 