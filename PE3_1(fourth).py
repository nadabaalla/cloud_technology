"""
Sort three input numbers. Save the code as PE3_4.py.
a) Prompt and request three integer numbers one by one from the console.
b) Sort these numbers and print them from smallest to largest.
Input text can be any content. Just make sure to precisely match the output format below.
Hint: You can use the built in functions max() and min()
"""
first=(input("Please enter the first integer: "))
second=(input("Please enter the second integer: "))
third=(input("Please enter the third integer: "))
totalnum = first, second, third
print('Before sorting: ', totalnum)
print('After sorting: ', sorted(totalnum))