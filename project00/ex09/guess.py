
# --------------------------------------------------------------------------------
# : color code
RED = '\033[91m'
GRE = '\033[92m'
YEL = '\033[93m'
BLU = '\033[94m'
MAG = '\033[95m'
CYA = '\033[96m'
RES = '\033[0m'
BOL = '\033[1m'
UND = '\033[4m'
# --------------------------------------------------------------------------------

print(f'''{YEL}This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type {BOL}'exit'{BOL} to end the game.{BOL}
{GRE}Good luck!{BOL}''')

# --------------------------------------------------------------------------------

count = True

while(count):

    input_value = input(f"{MAG}What's your guess between 1 and 99? {RES}")

    if input_value.lower() == "exit":
        print(f"{CYA}{BOL}Good buy!{RES}")
        break

    try:
        input_value = int(input_value)
    except ValueError:
        input_value = input(f"{RED}That's not a number.{RES} Press Enter to continue ")
        continue
    
    if input_value < 42:
        print(f"{YEL}{BOL}Too low!{RES}")
    if input_value > 42:
        print(f"{BLU}{BOL}Too hight!{RES}")
    if input_value == 42:
        print(f"{GRE}{BOL}You win!{RES}")
        break

