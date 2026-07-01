n1=int(input("enter the 1st number:"))
n2=int(input("enter the 2nd number:"))
op=input("enter the operator +,-,*,/:")
if op=="+":
    print("addition:",n1+n2)
elif op=="-":
    print("substraction:",n1-n2)
elif op=="*":
    print("multiplication:",n1*n2)
elif op=="/":
    print("division:",n1/n2)
else:
    print("invalid operator")