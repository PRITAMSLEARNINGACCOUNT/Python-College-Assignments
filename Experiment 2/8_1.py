Time = int(input("Enter The Time Period?\n"))
Principal = float(input("Enter The Principal Amount??\n"))
Rate = float(input("Enter The Interest Rate??\n"))
Interest = 0.0
for i in range(Time):
    Interest = ((Principal*Rate)/100)
    Principal += Interest
print(f"So The Compound Interest Amount Is {Interest+Principal}")
