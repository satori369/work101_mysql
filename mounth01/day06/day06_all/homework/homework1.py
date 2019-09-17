list_result = []
while True:
    str_input = input('请输入：')
    if str_input == '':
        break
    list_result.append(str_input)

str_result = '\n'.join(list_result)
print(str_result)