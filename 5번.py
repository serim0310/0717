# 홀수/짝수 판별기 함수, 매개변수 입력에 따라 홀수 또는 짝수를 자동으로 판별하는 함수를 작성하시오. 반환되는 값은 '홀수' 또는 '짝수'

def num(x) :
    result = ""

    if x % 2 == 0 :
        result = "짝수"

    else :
        result = "홀수"

    return result

number = num(1111)
print(number)