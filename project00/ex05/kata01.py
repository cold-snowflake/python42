#colors

CYAN = "\033[0;36m"
LIGHT_BLUE = "\033[1;34m"
ITALIC = "\033[3m"
END = "\033[0m"

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for key, values in kata.items():
    print(f"{CYAN}{ITALIC}{key}{END} was created by {LIGHT_BLUE}{values}{END}")