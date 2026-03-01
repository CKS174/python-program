medical_cause = input("Did you have a medical cause? (Yes/No) ").strip().upper()



if medical_cause == "Yes":
    print("you are allowed")
else:
    atten = int(input("Enter the attendence of the selected student:"))


    if atten >=75:
        print("You are allowed")
    else:
        print("You are not allowed")
