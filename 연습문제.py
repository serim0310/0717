def score(x) :
    result = ""

    if 81 <= x <= 100 :
        result = "A"
    elif 61 <= x <= 80 :
        result = "B"
    elif 41 <= x <= 60 :
        result = "C"
    elif 21 <= x <= 40 :
        result = "D"
    elif 0 <= x <= 20 :
        result = "E"

    return result

sc = int(input('점수를 입력하세요 : '))
res = score(sc)