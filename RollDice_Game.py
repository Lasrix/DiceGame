import random
import time

delay = 0.5

counter = 0

def next_steps():
    roll_result = random.randint(1, 100) 
    return roll_result

while True:
    wanna_play = input("We're gonna roll a dice. Below or equal to 50, you win. Otherwise, you lose. Ready? :").lower()

    if wanna_play == "yes":
        result = next_steps()
        if result <= 50:
            counter += 1
            print(f"You rolled a {result}")
            time.sleep(delay)
            print(f"Your score is now {counter}")
        else:
            print(f"You rolled a {result}")
            time.sleep(delay)
            print(f"You lose with a score of {counter}")
            break
    else:
        print(f"Fine. You lose with a score of {counter}")
        break
