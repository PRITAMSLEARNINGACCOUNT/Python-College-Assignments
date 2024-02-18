Mean = 0
Total = int(input("Enter How Many Numbers Do You Want To Calculate Mean?\n"))
for i in range(Total):
    Temp = int(input("Enter An Integer Number?\n"))
    Mean += Temp
Mean /= Total
print("So The Mean Of All The Numbers Given Is ", format(Mean, ".2f"))
