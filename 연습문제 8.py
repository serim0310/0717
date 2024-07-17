# 문자 길이에 대한
def find_len(x) :
    result = 0

    if len(x) <= 20:
        result = 50

    elif len(x) > 20:
        result = 100

    return result

text = input("문자를 입력해주세요 : ")
var = find_len("임의의 값")
print(var)