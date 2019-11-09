import sys
args = sys.argv  # a list of the arguments provided (str)
print("running two_digits.py", args)
a, b = int(args[1]), int(args[2])
print(a, b, a + b)