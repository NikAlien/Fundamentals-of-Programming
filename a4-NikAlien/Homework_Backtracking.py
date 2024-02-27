"""

    Consider the natural number n (n<=10) and the natural numbers a1, ..., an.
    Determine all the possibilities to insert between all numbers a1, ..., an the operators + and –
    such that by evaluating the expression the result is positive.

"""
import random

#Creating the list of random numbers
def create_list():
    print("How long would you like the list to be?")
    print("Note: n <= 10")
    nr = int(input("--> "))

    li = []
    for i in range(nr):
        li.append(random.randint(0, 100))

    print("\nYour list: ")
    print(li, "\n")
    return li


# Recursive solution to the problem through backtracking
def backtracking_rec(li, result, sum, i):
    # Checking if we found the solution or if we went out of the parameters
    if i == len(li) and sum > 0:
        print(*result, sep = ' ', end = ' ')
        print("= ", sum)
        return
    elif i == len(li):
        return

    # Initialyzing the first elements
    if i == 0:
        result.append(li[i])
        sum += li[i]
        i += 1

    # Checking the version with "+"
    result.append("+")
    result.append(li[i])
    backtracking_rec(li, result, sum + li[i], i + 1)
    result.pop()
    result.pop()

    # Checking the version with "-"
    result.append("-")
    result.append(li[i])
    backtracking_rec(li, result, sum - li[i], i + 1)
    result.pop()
    result.pop()


# Iterative solution to the problem
def iterative(li):
    n = len(li) - 1
    i = 0
    # Creating the lists
    while i < 2 ** n:
        sum = li[0]
        result = [li[0]]
        k = i
        for j in range(n):
            # Choosing the option
            if k % 2 == 0:
                result.append("+")
                result.append(li[j + 1])
                sum += li[j + 1]
            else:
                result.append("-")
                result.append(li[j + 1])
                sum -= li[j + 1]
            k = k // 2
        if sum > 0:
            print(*result, sep=' ', end=' ')
            print("= ", sum)
        result.clear()
        i += 1


def start():

    while True:
        print("\nResolve the problem: ")
        print("1. Recursive (backtracking)")
        print("2. Iterative")
        print("3. Exit")
        choice = input("--> ")

        if choice == "1":
            nr_list = create_list()
            print("Results: ")
            backtracking_rec(nr_list, [], 0, 0)
        elif choice == "2":
            nr_list = create_list()
            print("Results: ")
            iterative(nr_list)
        elif choice == "3":
            break
        else:
            print("Unidentifiable comment")


start()