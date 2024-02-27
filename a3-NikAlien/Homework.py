import random
import time

def generate_list(nr, k): #Generating the list of numbers

    fin = []
    if k == 1:
        for i in range(nr):
            fin.append(nr - i)
    elif k == 2:
        for i in range(nr):
            fin.append(random.randint(0, nr))
    elif k == 3:
        for i in range(nr):
            fin.append(i)

    print("\nYour list:")
    print(fin)
    return fin

def sort_cocktail(li): #Cocktail Sort
    s = 0
    e = len(li) - 1
    swap = True

    while swap:

        # Going through the list from right to left
        swap = False
        for i in range(s, e):
            if li[i] > li[i + 1]:
                aux = li[i]
                li[i] = li[i + 1]
                li[i + 1] = aux
                swap = True

        if swap == False:
            break
        # Going through the list from left to right
        swap = False
        e = e - 1
        for i in range(e - 1, s - 1, -1):
            if li[i] > li[i + 1]:
                aux = li[i]
                li[i] = li[i + 1]
                li[i + 1] = aux
                swap = True

        s = s + 1

def sort_gnome(li): #Gnome Sort
    n = len(li)
    i = 0

    while i < n:
        if i == 0:
            i = i + 1

        # Verifying two elements from the list and doing the according actions
        if li[i] >= li[i - 1]:
            i = i + 1
        else:
            aux = li[i]
            li[i] = li[i - 1]
            li[i - 1] = aux
            i = i - 1

def start():

    nr_list = []
    while True:
        print("\nMake your choice: ")
        print("1 - Generate a list of random numbers for the 2 and 3 option")
        print("2 - Sort the list using the Cocktail Sort")
        print("3 - Sort the list using the Gnome Sort")
        print("4 - Analyze the behavior of these algorithms in Worst Case")
        print("5 - Analyze the behavior of these algorithms in Average Case")
        print("6 - Analyze the behavior of these algorithms in Best Case")
        print("7 - Exit the program")

        choice = input("--> ")
        if choice == "1":
            n = int(input("Offer the number of natural numbers to generate --> "))
            nr_list = generate_list(n, 2)
        elif choice == "2":
            sort_cocktail(nr_list)
            print("\nFinal result: ")
            print(nr_list)
        elif choice == "3":
            sort_gnome(nr_list)
            print("\nFinal result: ")
            print(nr_list)
        elif choice == "4":
            n = int(input("Offer the first number of natural numbers to generate --> "))
            for i in range(5):
                nr_list = generate_list(n, 1)

                s_list = nr_list[:]
                start1 = time.time()
                sort_cocktail(s_list)
                end1 = time.time()
                t_ms = "{:.3f}".format((end1 - start1) * 1000)
                print("\nCocktail Sort: ", n, " terms - ", t_ms, " milliseconds")

                s_list = nr_list[:]
                start2 = time.time()
                sort_gnome(s_list)
                end2 = time.time()
                t_ms2 = "{:.3f}".format((end2 - start2) * 1000)
                print("Gnome Sort: ", n, " terms - ", t_ms2, " milliseconds\n")

                n *= 2
        elif choice == "5":
            n = int(input("Offer the first number of natural numbers to generate --> "))
            for i in range(5):
                nr_list = generate_list(n, 2)

                s_list = nr_list[:]
                start1 = time.time()
                sort_cocktail(s_list)
                end1 = time.time()
                t_ms = "{:.3f}".format((end1 - start1) * 1000)
                print("\nCocktail Sort: ", n, " terms - ", t_ms, " milliseconds")

                s_list = nr_list[:]
                start2 = time.time()
                sort_gnome(s_list)
                end2 = time.time()
                t_ms2 = "{:.3f}".format((end2 - start2) * 1000)
                print("Gnome Sort: ", n, " terms - ", t_ms2, " milliseconds\n")

                n *= 2
        elif choice == "6":
            n = int(input("Offer the first number of natural numbers to generate --> "))
            for i in range(5):
                nr_list = generate_list(n, 3)

                s_list = nr_list[:]
                start1 = time.time()
                sort_cocktail(s_list)
                end1 = time.time()
                t_ms = "{:.3f}".format((end1 - start1) * 1000)
                print("\nCocktail Sort: ", n, " terms - ", t_ms, " milliseconds")

                s_list = nr_list[:]
                start2 = time.time()
                sort_gnome(s_list)
                end2 = time.time()
                t_ms2 = "{:.3f}".format((end2 - start2) * 1000)
                print("Gnome Sort: ", n, " terms - ", t_ms2, " milliseconds\n")

                n *= 2
        elif choice == "7":
            break
        else:
            print("Unidentifiable comment")

start()