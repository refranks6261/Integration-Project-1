# Ryan Franks
# Body Mass Index, or BMI, is a way of describing height and weight in one number that can tell if someone's
# weight is healthy.  The universal formula developed by Belgium statistician, Adolphe Quetelet, in the 1800's
# is:  Multiply your weight in pounds by 703 and divide by your height (inches) squared.

# Introduction
print("Hello!  I am your friendly weight health calculator.  My job is to tell you your Body Mass Index, ")
print("or BMI.  I will also tell you if you are above or below the normal BMI range, and how much weight you ")
print("need to lose or gain in order to get into the normal range.")
print()
print("Are you ready to get started?")
print("Good!  Please enter the following information for me:")
print()

# Input request
# Input height in inches
num_height = int(input("Enter your Height in inches: "))
# Error check input num_height is between 36 and 84 inches with 3 tries to put in correct height
count = 1
while num_height < 36 or num_height > 84:
    count += 1
    if count < 4:
        print("You only get 3 tries.  You are on try:  ", count)
        num_height = int(input("Enter your REAL Height between 36 and 84 inches: "))
    else:
        print("Too many tries.")
        exit()
# Input weight in pounds
num_weight = int(input("Enter your Weight in pounds: "))
# Error check input num_weight is between 50 and 550 lbs with 3 tries to put in correct weight
count = 1
while num_weight < 50 or num_weight > 550:
    count += 1
    if count < 4:
        print("You only get 3 tries.  You are on try:  ", count)
        num_weight = int(input("Enter your REAL Weight between 50 and 550 pounds: "))
    else:
        print("Too many tries.")
        exit()
# Input gender m for Male or f for Female
str_gender = str(input("Enter your Gender.  Please use 'm' for Male and 'f' for Female: "))
# Make str_gender lowercase
str_gender = str_gender.lower()
# Error check input str_gender is 'm' or 'f' with 3 tries to input correct letter
count = 1
while str_gender != "m" and str_gender != "f":
    count += 1
    if count < 4:
        print("You only get 3 tries.  You are on try:  ", count)
        str_gender = str(input("Please use 'm' for Male and 'f' for Female: "))
        str_gender = str_gender.lower()
    # 3 try limit, add 1 to number of tries
    else:
        print("Too many tries.")
        exit()
# Input age in years
num_age = int(input("Enter your Age in years: "))
# Error check input num_age is between 18 and 108 with 3 tries to put in correct age
count = 1
while num_age < 18 or num_age > 108:
    count += 1
    if count < 4:
        print("You only get 3 tries.  You are on try:  ", count)
        num_age = int(input("Enter your Age between 18 and 108: "))
        # 3 try limit, add 1 to number of tries
    else:
        print("Too many tries.")
        exit()
print()
print("Thank you!")
print()

# BMI related output
print("The BMI ranges are the following:")
print("     Obese = 30 or Above")
print("     Overweight = 25.0 to 29.9")
print("     Normal Weight = 18.5 to 24.9")
print("     Underweight = Under 18.5")
print()
# Calculate BMI = (Weight * 703)/Height^2
bmi_number = float((num_weight * 703) / num_height ** 2)
# Categorize BMI into Obese, Overweight, Normal and Underweight
if bmi_number >= 30:
    print("Your BMI is in the Obese range at:  ", format(bmi_number, ".1f"), sep="")
elif 25.0 <= bmi_number <= 29.9:
    print("Your BMI is in the Overweight range at:  ", format(bmi_number, ".1f"), sep="")
elif 18.5 <= bmi_number <= 24.9:
    print("Your BMI is in the Normal range at:  ", format(bmi_number, ".1f"), sep="")
elif bmi_number < 18.5:
    print("Your BMI is in the Underweight range at:  ", format(bmi_number, ".1f"), sep="")
else:
    print("Your BMI can't be calculated.")
    exit()
print()
print(
    "Guess what?  If you are above or below what is considered 'Normal' "
    "I can tell you how much weight to gain or lose.")
print()

# Calculate weight needing to gain or lose by using the algebraically reworked BMI formula:
# num_weight_ideal is the ideal weight for the 'Normal' range = (Height^2 * BMI Normal Constant 21.7)/703
# One-time calculation of BMI 'Normal' Constant was found by adding the Normal range values of 18.5 and 24.9 and
# dividing by 2 to get 21.7
num_bmi_const = float(18.5 + 24.9) / 2
num_weight_ideal = int((num_height ** 2 * num_bmi_const) / 703)
# Categorize the weight that has to gain or has to lose from the ideal weight
if 18.5 <= bmi_number <= 24.9:
    print("Your BMI is in the Normal range.  You don't have to lose or gain any weight.")
elif bmi_number < 18.5:
    # New variable, num_weight_change = the ideal weight for 'Normal" range minus input weight
    num_weight_change = int(num_weight_ideal - num_weight)
    print("You need to gain weight.")
    print("Here is how much weight you need to gain: ", format(num_weight_change, "d"), "LBS", sep=" ")
elif bmi_number > 24.9:
    # New variable, num_weight_change = the weight input minus the ideal weight for 'Normal' range
    num_weight_change = int(num_weight - num_weight_ideal)
    print("You need to lose weight.")
    print("Here is how much weight you need to lose: ", format(num_weight_change, "d"), "LBS", sep=" ")
else:
    print("The amount of weight you need to lose or gain can't be calculated.")
    exit()
print()
