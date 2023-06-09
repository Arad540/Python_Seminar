a = int(input("Put 1st number: "))
b = int(input("Put 2nd number: "))


def recursive_sum(a, b):
    if a == 0:
        return b
    else:
        return recursive_sum(a - 1, b + 1)


print(recursive_sum(a, b))