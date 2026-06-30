
#user input
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Annual Rate (%): "))
time = float(input("Enter Time (Years): "))

#formulas
amount = principal * (1 + rate / 100) ** time
ci = amount - principal

#total value and interest amount
print("Compound Interest =", round(ci, 2))
print("Total Amount =", round(amount, 2))