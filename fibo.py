def fibo(data):
    if data <= 2:
        return 1
    return fibo(data-1) + fibo(data-2)



if __name__=="__main__":
    data = int(input("숫자를 입력하세요: "))
    print(fibo(data))
