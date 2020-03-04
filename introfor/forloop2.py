#!/usr/bin/env python3

# create a list of strings
vendors = ["cisco", "juniper", "big_ip", "F5", "arista"]

# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]

# loop across the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="")   # new line, print the current vendor, and end without new line
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")
