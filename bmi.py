def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi= weight/(height**2)
    if bmi < 18.5:
        print("You are Under Weight. Your BMI is: " + str(bmi))
        return -1
    elif bmi  <= 25.0:
        print("You are Acceptable. Your BMI is: " + str(bmi))
        return 0 
    else:
        print("You are Overweight. Your BMI is: " + str(bmi)) 
        return 1
print(calculate_bmi(weight=107, height=1.73))
