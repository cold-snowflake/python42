import sys

print(f"""
    Sum: {int(sys.argv[1]) + int(sys.argv[2])}
    Difference: {int(sys.argv[1]) - int(sys.argv[2])}
    Product: {int(sys.argv[1]) * int(sys.argv[2])}
    Quotient: {int(sys.argv[1]) / int(sys.argv[2])}
    Remainder: {int(sys.argv[1]) % int(sys.argv[2])}
""")