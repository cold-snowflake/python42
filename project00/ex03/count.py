def  text_analyzer(text):
    count_char = 0
    count_upper = ""
    count_lower = ""
    count_punct = ""
    count_space = 0

    for char in text:

        if(char.isupper()):
            count_upper += char

        if(char.islower()):
            count_lower += char

        if (ord(char) >= 33 and ord(char) <= 47):
            count_punct += char
    
    count_char = len(text)
    count_space = text.count(" ")
    
    print(f"""The text contains {count_char} character(s):
          - {len(count_upper)} upper letter(s)
          - {len(count_lower)} lower letter(s)
          - {len(count_punct)} punctuation mark(s)
          - {count_space} space(s)""")

if __name__ == "__main__":
    text_analyzer()