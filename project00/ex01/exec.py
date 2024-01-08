import sys
result = " ".join(str(item) for item in sys.argv[1:])
print(result[::-1])

