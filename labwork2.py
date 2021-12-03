# find BMI of a person where take mass and height as input from the user
#BIM =mass in kg / (height in m)2
M = int(input("enter the mass of person per kg:"))
H = int(input("enter the height of a person in meter:"))
BMI = (M / (H * H))
print(f"the BMI value of the person is {BMI}")


