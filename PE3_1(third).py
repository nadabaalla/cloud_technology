"""
Calculate the BMI. Save the code as PE3_3.py.
a) Prompt and request the input for height(cm) and weight(kg) from the console.
b) Compute the body mass index and print it in three decimal places.
"""
height=float(input("Please enter the height (in cm):"))
weight=float(input("Please enter the weight (in kg):"))
bmi= (weight/height**2)*703
print("BMI: ", (round(bmi,3)))

