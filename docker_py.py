import time

active = True
i = 0


while active:
    print("Hello world")
    time.sleep(2)
    i += 1

    if i == 10:
        active = False

