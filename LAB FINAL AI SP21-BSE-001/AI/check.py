def parent():
    a=int(input("Enter First Value: "))
    b=int(input("Enter Second Value: "))
    c=int(input("Enter 1 For Addition 2 For Multiplication : "))
        
    def perform(a,b,c):
        if (c==1):
            result=a+b
            print(result)
        
        elif (c==2):
            result=a*b
            print(result)
        
        else:
            result=0

    perform(a,b,c)

parent()