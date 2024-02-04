import sys
import string

def remove_punctuation(input_string):
    no_punct = ""
    for char in input_string:
        if char not in string.punctuation:
            no_punct += char
    return no_punct

try:
    count = int(sys.argv[2])
except ValueError:
    print("Error")
    sys.exit()

my_string = remove_punctuation(sys.argv[1])
my_string = my_string.split(" ")
result = [item for item in my_string if len(item) >= count]
print(result)
