#!/usr/bin/env python3


def same_necklace(a,b):
    if a == b:
        return True
    word = a
    for i in range(len(a)):
        word = word[1:]+word[0]
        if word == b:
            return True
    return False

def bonus1(a):
    if a == "":
        return 1
    word = a
    count = 0 
    for i in range(len(a)):
        if word == a:
            count += 1
        word = word[1:]+word[0]
    return count

def main():
    print("Please give me two strings. I will let you know if they belong to the same necklace.")
    a = input()
    b = input()

    print("Now give me another string. I will tell you how many times that string can repeat itself if scrambled")
    c = input()

    ret = same_necklace(a,b)
    count = bonus1(c)

    if(ret):
        print("These strings belong to the same necklace")
    else:
        print("These strings do not belong to the same necklace.")
    print("The first string repeats " + str(count))
main()
