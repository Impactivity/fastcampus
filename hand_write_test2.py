# 문제
# 하나의 문자열과 라인 길이를나타내는 숫자가 주어지고,
# 라인 길이만큼 문자열을 짜르고 줄바꿈 기호를 넣되, 문자열 안에 스페이스가 있을 경우 보기 좋게 하기 위해, 스페이스가 있는 부분에서 줄바꿈
# 기호를 넣도록 코드를 구현하라

# 여기에서 코드를 작성하기전에 문제에 구체적으로 언급되지 않았던 조건들에 대해 질문하라!
# 1. 입력에는 null이 들어오는가 ,
# 2. 입력 문자열의 종류는 어떠한가
# 3. 입력형태는 어떻게 주어지는가 ( 문자열 숫자, 또는 문자열 \n 숫자,  문자열 콤마 숫자 인지 판단)
# 4. 문자열의 길이는 최대 몇이고 Max_line 수 최대는 몇?


import sys
read = sys.stdin.readline
input_string = read()
# input_string2 = list(read().rstrip().split())
max_line = int(read())


def line_edit(string, max_line):
    if string == None or max_line == None or len(string) < max_line:
        return string

    for index in range(max_line - 1, 0, -1):
        if string[index] == ' ':
            return string[:index] + '\n' + line_edit(string[index:].lstrip(), max_line)
    return string[:max_line] + '\n' + line_edit(string[max_line:].lstrip(), max_line)


# 처음에 짠 코드 
def edit_line(arr):
    if len(arr) == 0:
        return False

    for line in arr:
        if len(line) < max_line:
            print(line)
        else:
            cnt = 0
            for i in range(len(line)):
                if cnt < max_line:
                    print(line[i] , end = '')
                    cnt += 1
                else:
                    print('')
                    print(line[i], end='')
                    cnt = 1
            print('')

# edit_line(input_string2)

tmp_arr = line_edit(input_string,max_line)
print(tmp_arr)