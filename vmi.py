height = float(input("enter your height in cm:"))
weight = float(input("enter your weight in kg:"))


BMI = weight / (height/100)**2

print("your BMI is", BMI)

if BMI <= 18.4:
    print("your weight is under 18.4 classing  you as under weght.")
elif BMI <= 24.9:
    print("you are healthy.")
elif BMI <= 29.9:
    print("your weight is over 24.9 classing you as over weight.")
elif BMI <= 34.9:
    print("you are over the weight of 29.9 classing you as severeley over weight.")
elif BMI <=39.9:
    print("your weight is over 34.9 classing you as obese.")
else:
    print("your weigt is over 39.9 classing you as severlely obese.")
