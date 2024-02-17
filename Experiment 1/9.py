Days=int(input("Enter Total Number Of Days??\n"))
Year=0
Month=0
while(Days>=365):
    Year+=1
    Days=Days-365
while(Days>=60):
    Month+=1
    Days=Days-60
print(str(Year) +" Year "+str(Month)+" Months "+" & "+ str(Days)+" Days")
    