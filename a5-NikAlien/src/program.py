#
# Write the implementation for A5 in this file
#
import random
import math

import numpy as np


#
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

# Create new element
def new_cnr(r, i):
    r = math.floor(r)
    i = math.floor(i)
    return [r, i]


# Get the real part of the element
def get_real(nr):
    return nr[0]


# Get imaginary part of the element
def get_img(nr):
    return nr[1]


# Transform element to string to be displayed
def list_str(nr):
    if nr[0] == 0:
        if nr[1] == 0:
            return "z = 0"
        else:
            return "z = " + str(nr[1]) + "i"
    elif nr[1] == 0:
        return "z = " + str(nr[0])
    else:
        if nr[1] > 0:
            return "z = " + str(nr[0]) + " + " + str(nr[1]) + "i"
        else:
            return "z = " + str(nr[0]) + " - " + str(abs(nr[1])) + "i"


#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

# def new_cnr(r, i):
#     r = math.floor(r)
#     i = math.floor(i)
#     return {"real": r, "img": i}
#
#
# def get_real(nr):
#     return nr["real"]
#
#
# def get_img(nr):
#     return nr["img"]
#
#
# def list_str(nr):
#     if nr["real"] == 0:
#         if nr["img"] == 0:
#             return "z = 0"
#         else:
#             return "z = " + str(nr["img"]) + "i"
#     elif nr["img"] == 0:
#         return "z = " + str(nr["real"])
#     else:
#         if nr["img"] > 0:
#             return "z = " + str(nr["real"]) + " + " + str(nr["img"]) + "i"
#         else:
#             return "z = " + str(nr["real"]) + " - " + str(abs(nr["img"])) + "i"


#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# set A: Length and elements of the longest subarray of numbers where their real part is in the form of a mountain
# set B: The length and elements of the longest increasing subsequence, when considering each number's modulus
# -> There should be no print or input statements in this section wc
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

# Add element to current list
def add_nr(li, new):
    li.append(new)
    return li


# Generator of random numbers for initial list
def generate_random(n):
    ran_list = []

    for i in range(n):
        r = random.randint(-10, 10)
        i = random.randint(-10, 10)
        ran_list.append(new_cnr(r, i))

    return ran_list


# Finding the longest mountain subarray using a non-optimized version
def mountain_subarray(comp_nr):
    fin = []
    n = len(comp_nr)

    for i in range(n - 1):
        for j in range(i + 2, n):
            # Creating all possible sub-arrays
            subarray = comp_nr[i:j + 1]

            # Going through them and checking if they have a mountain shape
            index = 0
            l = len(subarray)
            while index < l - 1 and get_real(subarray[index]) < get_real(subarray[index + 1]):
                index += 1
            if index != 0 or index != l - 1:
                while index < l - 1 and get_real(subarray[index]) > get_real(subarray[index + 1]):
                    index += 1
                if index == l - 1:
                    if l > len(fin):
                        fin = subarray[:]

    return fin


# Complex numbers modulus
def modulus_comp(nr):
    return math.sqrt(get_real(nr) ** 2 + get_img(nr) ** 2)


# Getting the largest subsequence according to the modulus using dynamic programming
def increasing_sub(comp_nr):
    n = len(comp_nr)
    li = [0] * n
    fin = []
    index = 0

    # Finding all possible increasing subsequences
    for i in range(n):
        for j in range(i):
            if modulus_comp(comp_nr[i]) > modulus_comp(comp_nr[j]):
                li[i] = max(li[i], li[j] + 1)
        if li[i] == index:
            fin.append(comp_nr[i])
            index += 1

    return fin


#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

# The menu
def menu():
    print("\n1. Add a new complex number to the list")
    print("2. Display the existing list (there are already 10 available elements in the list)")
    print(
        "3. Display the length and elements of the longest subarray where their real part is in the form of a mountain")
    print(
        "4. Display the length and elements of the longest increasing subsequence, when considering each number's modulus")
    print("5. Exit the program")


# Reading a complex number
def read_nr():
    print("\nWrite your complex number\nformat: a + bi\na, b - integer")
    string = input("z = ")
    string = string.replace(" ", "").replace("i", "j")
    nr = complex(string)
    return new_cnr(np.real(nr), np.imag(nr))


# Displaying the list
def display_list(li):
    n = len(li)
    if n == 0:
        print("\n There is no element in the list")
    else:
        print("\nYour list: ")
        for i in range(n):
            print(list_str(li[i]))

        print("Length of the list is ", len(li))


# The start
def start():
    # TODO: multiple functions from choice 1, 3, 4 can be put together
    # Use better var name (fin - not good)
    nr_list = generate_random(10)

    while True:
        menu()
        choice = input("--> ")

        if choice == "1":
            new_nr = read_nr()
            nr_list = add_nr(nr_list, new_nr)
        elif choice == "2":
            display_list(nr_list)
        elif choice == "3":
            result = mountain_subarray(nr_list)
            display_list(result)
        elif choice == "4":
            result = increasing_sub(nr_list)
            display_list(result)
        elif choice == "5":
            break
        else:
            print("\nUnidentifiable comment")


if __name__ == "__main__":
    start()