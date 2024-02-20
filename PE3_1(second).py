"""
Calculates the amount of a server’s tip. Save the code as PE3_2.py.
a) Prompt and request input the amount of the bill (in float) and the percentage of tip (in integer).
b) Calculate, set the result to two decimal places and print the result.
Input text can be any content. Just make sure to precisely match the output format below
"""
bill=float(input("Enter the bill amount :$"))
tip=int(input("Enter the tip percentage: "))
tipAmount= (tip/100)*bill
print("Tip Amount: $", (round(tipAmount,2)))
total= (bill+tipAmount)
print("Total: $", (round(total,2)))
