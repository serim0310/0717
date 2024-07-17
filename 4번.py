# 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 리스트로 반환하는 함수를 작성하시오.

number = [100, 200, 300]

def VAT(number) :
    result = []

    for num in number :
        result.append(int(num * 0.1 + num))

    return result

print(VAT(number))