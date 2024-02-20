#1_a
print("012345678901234567890")
print ('A' .rjust(5), 'B' .center(5), 'C' .ljust(5), sep = "**")
#012345678901234567890
#    A*  B  *C
#1_b
print("01234567890123456")
print("{0:^7}{1:4}{2:>6s}".format("one", "two", "three"))
print(f"{'one':^7}{'two':4}{'three':>6s}")
#01234567890123456
#  one  two  three
#  one  two  three
