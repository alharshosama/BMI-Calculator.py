## اسامة محمد صالح الهرش


def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) given weight in kilograms and height in meters.
    Formula: BMI = weight / (height * height)
    """
    bmi = weight / (height * height)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value and provide a corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Get user input for weight and height
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Interpret BMI
category = interpret_bmi(bmi)

# Print the calculated BMI and category
print("BMI: {:.2f}".format(bmi))
print("Category: ", category)
