"""
This is a faulty calculator and these are wrong values 
5+5=15, 4-1=4, 2*2=3
"""


s = "YES"

while s == "YES":
    print("Enter the first  number:")
    a = int(input())

    print("Enter +, -, *, / :")
    o = input()

    # if(o!="+" or o!="-" or o!="*"or o!="/"):
    #     print("Enter +, -, *, / :")
    #     o = input()
    
    print("Enter the second  number:")
    b = int(input())

    # Faulty calculations
    if(a==5 and o=="+" and b==5 ):
        print("Answer is = ", 15)

    if(a==4 and o=="-" and b==1):
        print("Answer is = ", 4)

    if(a==2 and o=="*" and b==2):
        print("Answer is = ", 3)


    # Real calculations
    if(o=="+" and a!=5 and b!=5):
        print("Answer is = ", a+b)

    if(o=="-" and a!=4 and b!=1):
        print("Answer is = ", a-b)

    if(o=="*" and a!=2 and b!=2):
        print("Answer is = ", a*b)

    if(o=="/"):
        print("Answer is = ", a/b)

    # Eding the loop
    print("Do you want to use the calculator? Type \"YES\" or \"NO\":")
    s = input()
    s = s.upper()

