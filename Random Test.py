import random
import time

while True:
    number = random.randint(1, 10)
    print(number)
    time.sleep(1)
    if number == 7:
        break
