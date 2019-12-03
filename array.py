#!/usr/bin/env python3

# Plagarized by : Teddy Sannan
# Created on : December 02 2019
# This program uses arrays

import random


def main():
    # this function uses an array
    random_number = []
    number_of_integers = 10

    # output and process
    for loop_counter in range(0, 11):
        total = sum(random_number)
        random_numbers = (random.randint(1, 101))
        random_number.append(random_numbers)

    print("")
    print("Here are the Numbers:")
    for loop_counter in range(0, 10):
        average = total / number_of_integers
        print("{0} ".format(random_number[loop_counter]), end="")

    print('\n')
    print("Average is: {0}".format(average))


if __name__ == "__main__":
    main()
