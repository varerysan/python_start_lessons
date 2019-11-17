#!/usr/bin/env python3
# Check if two line are acromyns of each other

def checkAcronym(line1, line2):
    if len(line1) != len(line2):
        return False

    counter = {}

    for sym in line1:
        counter[sym] = counter.get(sym, 0) + 1

    for sym in line2:
        counter[sym] = counter.get(sym, 0) - 1

    return all( v == 0 for v in counter.values() )

def main():
    print("Test for acronym.")
    line1 = input("Input line1:")
    line2 = input("Input line2:")
    if checkAcronym(line1, line2):
        print("Yes. Lines are the same acronyms")
    else:
        print("No. Lines are not the same acronyms")

main()
