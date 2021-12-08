# WAP which accepts marks of four subjects and display total marks,
#  percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first division,
#  more than 40% –> pass, less than 40% –> fail



Subject1 = int(input ("enter the marks of  first subject: "))
Subject2 = int(input("enter the marks of  second subject: "))
Subject3 = int(input("enter the marks of third subject: "))
Subject4 = int(input("enter the marks of fourth subject: "))

sum = Subject1 + Subject2 + Subject3 + Subject4 
print(f"sum of all the subjects is {sum}")

percentage = sum / 4
print(f"percentage of all 4 subject is {percentage}")


grade = percentage / 25
print(f"the obtained grade is  {grade}")

if percentage >= 70:
    print("good you achieved distinction")
elif percentage >=60 and percentage < 70:
    print("you achieved first division")
elif percentage >= 40 and percentage <60:
    print("you are pass")
else:
    print("you are fail")
