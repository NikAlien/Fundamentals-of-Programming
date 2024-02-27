"""

Given the set of positive integers S and the natural number k, display one of the
subsets of S which sum to k.
For example, if S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14.

"""
from texttable import Texttable

# Printing the matrix with the memorized numbers
def mat_print(mat, n, m):
    t = Texttable()
    t.header(['X'] + list(range(m)))
    for i in range(n):
        t.add_row([i] + mat[i])
    print(t.draw())

# Creating the array with the final result
def create_result(tabel, array, i, k):
    fin = []
    fin.append(array[i - 1])
    k -= array[i - 1]
    i = 1

    # Going through the memorized tabel to get the necessary numbers
    while k > 0:
        while tabel[i][k] != k:
            i += 1
        fin.append(array[i - 1])
        k -= array[i - 1]
        i = 1
    fin.reverse()
    print("\nResult is: ")
    print(fin)

# Dynamic Programing _ solution to the problem
def sum_dp(k, array, n):

    # Creating the tabel of memorized numbers
    tabel = [[0 for i in range(k + 1)] for i in range(n + 1)]

    # Going through the tabel
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # For the sums smaller than the taken element we copy the above row
            if j < array[i - 1]:
                tabel[i][j] = tabel[i - 1][j]
            # For the sums + to the element we take a subset which contains only that particular element
            elif j == array[i - 1]:
                tabel[i][j] = array[i - 1]
            # For the other sums we take either the element above(in case we don't have a methode to compute it)
            # we add the element we are currently working with to another sum that we
            # or already computed s.t. we get our current sum
            else:
                tabel[i][j] = max(array[i - 1] + tabel[i - 1][j - array[i - 1]], tabel[i - 1][j])

            # In case we find our sum earlier we finish the process and exit the function
            if tabel[i][j] == k:
                mat_print(tabel, n + 1, k + 1)
                return tabel, i

    # In case we don't find the sum
    if i == n and j == k:
        if tabel[i][j] != k:
            print("\nNo result")
            return [[]], 0

def sum_naive(array, check):
    i = 1
    n = len(array)
    # Creating all possible subsets and verifying them
    while i <= 2 ** n:
        sum = 0
        result = []
        k = i
        for j in range(n):
            if k % 2 == 1:
                sum += array[j]
                result.append(array[j])
            k = k // 2
        if sum == check:
            print("\nResult is: ")
            print(result)
            break
        i += 1
    if i > 2 ** n:
        print("\nNo result")

def start():

    while True:
        # Menu
        print("\nResolve the problem: ")
        print("1. Dynamic programming")
        print("2. Non-optimized version")
        print("3. Exit")
        choice = input("--> ")

        array = []
        if choice == "1":
            print("How many elements in the list: ")
            n = int(input("--> "))
            print("Give an array: ")
            for i in range(n):
                nr = int(input())
                array.append(nr)

            print("Offer a sum: ")
            k = int(input("--> "))
            tab = [[]]
            tab, i = sum_dp(k, array, n)
            if i != 0:
                create_result(tab, array, i, k)

        elif choice == "2":
            print("How many elements in the list: ")
            n = int(input("--> "))
            print("Give an array: ")
            for i in range(n):
                nr = int(input())
                array.append(nr)

            print("Offer a sum: ")
            k = int(input("--> "))
            sum_naive(array, k)

        elif choice == "3":
            break
        else:
            print("\nUnidentifiable comment")

start()