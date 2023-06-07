a = int(input("Out the number: "))
b = int(input("Put power number: "))


def func(a, b):
    if b == 0:
        return 1

    return a * func(a, b - 1)


print(func(a, b))