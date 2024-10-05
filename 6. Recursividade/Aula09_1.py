def fatorial(x):
    print(x)
    if x == 1:
        return 1
    else:
        return x * fatorial(x - 1)


print(fatorial(8))