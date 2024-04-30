def calculate_bmi (height, weight):
    print("Height = " + str(height))
    print("Weigh = " + str(weight))
    BMI = weight/(height*height)
    print("BMI is " + str(BMI))
    if BMI < 18.5: 
        print(-1)
    elif 18.5<=BMI<=25:
        print(0)
    else:
        print(1)

calculate_bmi(weight = 57, height = 1.73)


