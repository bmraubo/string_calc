def Add(string):
    negatives_list = []

    def Empty(string):
        if string == "":
            return True

    def Negative(num):
        if int(num) < 0:
            negatives_list.append(int(num))

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
                        Negative(num)
                        answer += int(num)
                    if len(negatives_list) == 0:
                        return answer
                    else:
                        raise Exception(f'Negatives not allowed: {negatives_list}')
            elif Empty(string.split('\n')[1]):
                return 0
            else:
                answer = 0
                delimiter = string.split('\n')[0].strip('//')
                for num in string.split('\n')[1].split(delimiter):
                    Negative(num)
                    answer += int(num)
                if len(negatives_list) == 0:
                    return answer
                else:
                    raise Exception(f'Negatives not allowed: {negatives_list}')
        else:
            answer = 0
            for num in string.replace('\n',',').split(','):
                Negative(num)
                answer += int(num)
            if len(negatives_list) == 0:
                return answer
            else:
                raise Exception(f'Negatives not allowed: {negatives_list}')

if __name__ == '__main__':
    string = input('Enter string:')
    Add(string)