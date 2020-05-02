#!/usr/bin/env python3


def same_necklace(a,b):
    if a == b:
        return True
    word = a
    for i in range(len(a)):
        word = word[1:]+word[0]
        print(word)
        if word == b:
            return True
    return False

def main():
    print("Please give me two strings. I will let you know if they belong to the same necklace.")
    a = input()
    b = input()

    ret = same_necklace(a,b)

    if(ret):
        print("These strings belong to the same necklace")
    else:
        print("These strings do not belong to the same necklace.")

main()
