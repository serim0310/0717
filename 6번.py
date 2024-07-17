# 리스트 변수의 평균 값을 구하는 함수를 작성하시오. 리스트의 길이는 매번 달라질 수 있음에 유의하고, sum() 함수를 사용할 수 없다.

def mean_list(x) :
    result = 0

    for i in x :
        result = result + i
    avg = result / len(x)

    return avg

var = list(range(2, 99999))
print(mean_list(var))