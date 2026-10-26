a= float(input("Enter the numbers for Grades number/20 : "))
if a<=0 or a>20:
    print("Invalid Grades")
elif a>=16:
    print("Very Good")
elif a>=14 and a<16:
    print("Good")
elif a>=12 and a<14:
    print("Fairly Good")
elif a>=10 and a<12:
    print("Pass")
else:
    print("Fail")