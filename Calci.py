#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     11/09/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

first = input("enter the First number:")
operator = input("enter operator (+,-,/,*,%) :")

second = input("enter the Second number:")
first = int(first)
second = int(second)
if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "%" :
    print(first%second)
elif operator == "/" :
    print(first/second)
elif operator == "*" :
    print(first*second)
else:
    print("invalid condition")