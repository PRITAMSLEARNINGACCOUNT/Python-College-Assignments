Num_1=int(input("Enter First Number??\n"))
Num_2=int(input("Enter Second Number??\n"))
print("Enter '/' For Division\nEnter '*' For Multiplication\n Enter '+' For Addition\nEnter '-' For Subtraction\nEnter '//' For Quotient\nEnter ''**' For Exponent\nEnter '%' For Reminder\n")
# print(7%2)
Choice=input("Now Enter Your Choice Of Operation??\n")
if Choice=="/":
    print(f"So The Result After Division Is {Num_1/Num_2}")
elif Choice=="*":
    print(f"So The Result After Multiplication Is {Num_1*Num_2}")
elif Choice=="+":
    print(f"So The Result After Addition Is {Num_1+Num_2}")
elif Choice=="-":
    print(f"So The Result After Subtraction Is {Num_1-Num_2}")
elif Choice=="**":
    print(f"So The Result After Exponent Is {Num_1**Num_2}")
elif Choice=="//":
    print(f"So The Result After Quotient Is {Num_1//Num_2}")    
else:
    print(f"So The Result After Calculating Reminder Is {Num_1%Num_2}")

