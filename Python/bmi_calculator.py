#bmi : Body Mass index is a number used to estimate whether a person's weight is appropriate for their height
# bmi = Weight(kg) / Height (m)2
#Undernourished /Underweight       less than 18.5
#Average / NormalWeight              18.5 – 24.9
#obese                              30.0 – 39.9
#super obese                        40.0 and above



# Enter user weight in kilograms
weight = float(input("Enter Weight in Kg: "))

# Enter user height in meters
height = float(input("Enter Height in Meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI
print("BMI =",round (bmi, 2))

# Determine BMI category
if bmi < 18.5:
    print("Category: Undernourished")
elif bmi < 25:
    print("Category: Average")
elif bmi < 30:
    print("Category: obese")
else:
    print("Category:super Obese")



