#!/usr/bin/env python3
# cerner_2tothe5th_2021

from multiprocessing import Pool, cpu_count
import time

# recursive input sanitization
def user_check(count, prompt, right_answer):
    x = count
    # getting input
    answer = input(prompt).lower()
    # basic if statements for correct answer
    if answer not in right_answer and x <= 2:
        print(f"Sorry? '{answer}'?! You have been wrong {x} time(s)...")
        x += 1
        user_check(x, prompt, right_answer)
    elif answer not in right_answer and 2 < x < 4:
        print("Now you are just trying to fail. Thank carefully about your answer")
        x += 1
        user_check(x, prompt, right_answer)
    elif answer not in right_answer and 3 <= x < 5:
        print(f"You asked for it, all your CPU belongs to me...Calculating...")
        pool = Pool(cpu_count())
        pool.map(cpu_killer, range(cpu_count()))
        pool.close()
        x += 1
        user_check(x, "Do as I say! Now enter it right!: ", right_answer)

# pooled process to use all CPUs
def cpu_killer(x):
    # only lasts 5 seconds
    t_end = time.time() + 5
    while time.time() < t_end:
        x * x


if __name__ == '__main__':
    # trying to be funny and failing
    user_check(1, "Sigh... please enter true: ", {"true"})
    user_check(1, "Ohhh look a human did something right.. now enter the opposite of true: ", {"false"})
    user_check(1, "Whatever, not like I wanted this either, enter hotdogs: ", {"hotdogs"})
    user_check(1, "Please go away.. now do you want this to end?: ", {"true", "yes"})
    print("Finally..... goodbye")
