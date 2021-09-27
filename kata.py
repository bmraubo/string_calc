def add(string):
    negatives_list = []

    #Nested Functions
    def empty(string):
        if string == "":
            return True

    def negative(num):
        if int(num) < 0:
            negatives_list.append(int(num))
    
    def calculate(num_string):
        answer = 0 
        for num in num_string:
            negative(num)
            answer += int(num)
        if len(negatives_list) == 0:
            return answer
        else:
            raise Exception(f'Negatives not allowed: {negatives_list}')

    def custom_delimiter(string):
        if string.count('\n') > 1:
            if empty(string[4:]):
                return 0
            else:
                num_string = string[4:].split('\n')
                return calculate(num_string)
                
        elif empty(string.split('\n')[1]):
            return 0
        else:
            delimiter = string.split('\n')[0].strip('//')
            num_string = string.split('\n')[1].split(delimiter)
            return calculate(num_string)

    #Logic
    if empty(string):
        return 0
    elif string[:2] == '//':
        return custom_delimiter(string)
    else:
        num_string = string.replace('\n',',').split(',')
        return calculate(num_string)

if __name__ == '__main__':
    input_delimiter = input('Enter delimiter:')
    input_nums = input('Enter numbers seperated by delimiter:')
    print(add(f'//{input_delimiter}\n{input_nums}'))