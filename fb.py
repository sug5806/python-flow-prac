def fizzbuzz(a):
    if not a % 15:
        print("fizzbuzz")
    elif not a % 3:
        print("fizz")
    elif not a % 5:
        print("buzz")


if __name__=="__main__":
    for i in range(1, 101):
        fizzbuzz(i)
