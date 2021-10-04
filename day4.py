#!/usr/bin/env python3
from multiprocessing import Pool, cpu_count
import time

def user_check(count, prompt, right_answer):
    x = count
    answer = input(prompt).lower()
    if answer not in right_answer and x <= 2:
        print(f"Sorry? '{answer}'?! You were wrong for the {x} time...")
        x += 1
        user_check(x, prompt, right_answer)
    elif answer not in right_answer and 2 < x < 4:
        print("Now you are just trying to fail. Thank carefully about your answer")
        x += 1
        user_check(x, prompt, right_answer)
    elif answer not in right_answer and 3 <= x < 10:
        print(f"You asked for it, all your CPU belongs to me...Calculating...")
        pool = Pool(cpu_count())
        pool.map(cpu_killer, range(cpu_count()))
        pool.close()
        x += 1
        user_check(x, prompt, right_answer)


def cpu_killer(x):
    t_end = time.time() + 5
    while time.time() < t_end:
        x * x


if __name__ == '__main__':
    user_check(1, "Enter True: ", {"true"})
    user_check(1, "That was easy, enter the opposite of True: ", {"false"})
    user_check(1, "Please give me candy, enter snickers: ", {"snickers"})
    user_check(1, "Do you want to end this?: ", {"true", "yes", "end me"})
    print("Finally..... goodbye")
