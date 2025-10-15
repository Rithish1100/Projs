def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def divide(n1,n2):
    return(n1/n2)
operations={"+":add,"-":sub,"*":mul,"/":divide}
a=""
o='y'
while o=='y':
     a=input("enter the operation")
     b=float(input("enter the first number"))
     c=float(input("enter the second number"))
     res=operations[a](b,c)
     print(operations[a](b,c))
     o=input("would you like to continue type y")
     b=res
     c=float(input("enter the second number"))
     a=input("enter the operation")
     res=operations[a](b,c)
     print(operations[a](b,c))
     o=input("would you like to stop type n")
     if o=='n':
            res=o
            o='y'
            
