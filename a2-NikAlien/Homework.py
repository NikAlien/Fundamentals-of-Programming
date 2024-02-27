import random

def generate_list(): #Generating the list of random numbers

    n = int(input("Offer the number of natural numbers to generate --> "))
    fin = []

    for i in range(n):
        fin.append(random.randint(0, 100))

    print("\nYour list:")
    print(fin)
    return fin

def sort_cocktail(li, st): #Cocktail Sort
    s = 0
    ver = 0
    e = len(li) - 1
    swap = True

    while swap:

        #Going through the list from right to left
        swap = False
        for i in range(s, e):
            ver = ver + 1
            if li[i] > li[i + 1]:
                aux = li[i]
                li[i] = li[i + 1]
                li[i + 1] = aux1
                swap = True
            if ver % st == 0:
                print("\n", ver, " steps")
                print(li)

        if swap == False:
            break
        #Going through the list from left to right
        swap = False
        e = e - 1
        for i in range(e - 1, s - 1, -1):
            ver = ver + 1
            if li[i] > li[i + 1]:
                aux = li[i]
                li[i] = li[i + 1]
                li[i + 1] = aux
                swap = True
            if ver % st == 0:
                print("\n", ver, " steps")
                print(li)

        s = s + 1

def sort_gnome(li, st): #Gnome Sort
    n = len(li)
    i = 0
    ver = 0

    while i < n:
        if i == 0:
            i = i + 1

        #Verifying two elemnets from the list and doing the according actions
        if li[i] >= li[i - 1]:
            i = i + 1
            ver = ver + 1
        else:
            aux = li[i]
            li[i] = li[i - 1]
            li[i - 1] = aux
            i = i - 1
            ver = ver + 1

        if ver % st == 0:
            print("\n", ver, " steps")
            print(li)


def start():

    nr_list = []
    while True:
        print("\nMake your choice: ")
        print("1 - Generate a list of random numbers")
        print("2 - Sort the list using the Cocktail Sort")
        print("3 - Sort the list using the Gnome Sort")
        print("4 - Exit the program")

        choice = input("--> ")
        if choice == "1":
            nr_list = generate_list()
        elif choice == "2":
            step = int(input("Offer the number of steps at which you'll see the list during the sorting --> "))
            sort_cocktail(nr_list, step)
            print("\nFinal result: ")
            print(nr_list)
        elif choice == "3":
            step = int(input("Offer the number of steps at which you'll see the list during the sorting --> "))
            sort_gnome(nr_list, step)
            print("\nFinal result: ")
            print(nr_list)
        elif choice == "4":
            break
        else:
            print("Unidentifiable comment")

start()
