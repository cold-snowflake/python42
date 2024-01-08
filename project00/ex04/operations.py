import sys
if len(sys.argv) == 3:
    sum = int(sys.argv[1]) + int(sys.argv[2])
    product = int(sys.argv[1]) * int(sys.argv[2])
    difference = int(sys.argv[1]) - int(sys.argv[2])

if len(sys.argv) == 3 and int(sys.argv[2]) != 0:
    quotient = int(sys.argv[1]) / int(sys.argv[2])
    remainder = int(sys.argv[1]) % int(sys.argv[2])
else:
    quotient = " ERROR (division by zero)"
    remainder = " ERROR (modulo by zero)"
print(f"""
    Sum: {sum}
    Difference: {difference}
    Product: {product}
    Quotient: {quotient}
    Remainder: {remainder}
""")