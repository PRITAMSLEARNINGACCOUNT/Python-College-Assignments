Num_1 = int(input("Enter First Number??\n"))
Num_2 = int(input("Enter Second Number??\n"))
Num_3 = int(input("Enter Third Number??\n"))
Largest = 0
if Num_1 > Num_2:
    Largest = Num_1
else:
    Largest = Num_2
if Largest < Num_3:
    Largest = Num_3
print(f"{Largest} Is Greatest.")
