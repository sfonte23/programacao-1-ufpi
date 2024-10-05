import time


def contador(i):
    print(i)
    time.sleep(1)
    contador(i + 1)


contador(0)
# loop infinito