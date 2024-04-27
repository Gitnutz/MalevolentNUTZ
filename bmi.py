print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def calculate_bmi(height, weight):     
    print("Height = " + str(height)) 
    print("Weight = " + str(weight)) 
    bmi = weight/(height*height)
    print("BMI = " + str(bmi)) 
    if ( bmi < 18.5 ):
        print("Dude is Under Weight")
    if ( 18.5 < bmi < 25.0 ):
        print("Dude is Normal Weight")
    if ( bmi > 25.0 ):
        print("Dude is Over Weight")
calculate_bmi(weight=80, height=1.73)