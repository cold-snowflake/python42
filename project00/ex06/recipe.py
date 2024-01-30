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
cookboock = {
    "sandwich":
    {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": 
    {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad":
    {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "salad",
        "prep_time": 15
    }
}

# --------------------------------------------------------------------------------
#print all recipe names
def print_all_name_of_recipe(recipe_dic):
    print(f"{BOL}{RED}NAME OF RECIPE:{RES}")
    for key in recipe_dic:
        print(f"{MAG}{BOL}{key}{RES}",)

# print_all_name_of_recipe(cookboock)

# --------------------------------------------------------------------------------
#function that takes a recipe name and print its details

# name_of_recipe = input(f"{CYA}{BOL}Enter name of food:{RES} ")

def print_recipe_details(name_of_recipe):
    try:
        val = cookboock.get(name_of_recipe.lower())
        print(f"{BLU}{BOL}{name_of_recipe.upper()}{RES}\n{YEL}{UND}Ingredients{RES}: {val['ingredients']}")
        print(f"{BLU}To be eaten for {val['meal']}.{RES}")
        print(f"Takes {val['prep_time']} minutes of cooking.")
    except TypeError:
        print(f"{RED}{BOL}We don`t have a such recipe!{RES}")

# print_recipe_details(name_of_recipe)

# --------------------------------------------------------------------------------
#function that takes a recipe name and delete it.

# name_of_food = input(f"{BLU}{BOL}Enter name of food for deletion: {RES}")

def delete_cook(name_of_food):
    val = cookboock.get(name_of_food.lower())
    try:
        val.clear()
        print(f"{RED}{BOL}{name_of_food.lower()} deleted{RES}")
    except AttributeError:
        print(f"{RED}{BOL}We don`t have a such recipe!{RES}")

# delete_cook(name_of_food)

# --------------------------------------------------------------------------------
#function that add a recipe from user input.
        
# key_name = input(f"{BLU}{BOL}Enter your own name of food for adding: {RES}")
# ingredients_name = list(map(str, (input(f"{BLU}{BOL}Enter all ingredients: {RES}").lower().split())))
# meal_name = input(f"{BLU}{BOL}Enter type of meal: {RES}")

# try:
#     prep_time = int(input(f"{BLU}{BOL}Enter preperation time: {RES}"))
# except ValueError:
#     print(f"{RED}{BOL}Enter number!{RES}")
#     prep_time = int(input(f"{BLU}{BOL}Enter preperation time: {RES}"))

def add_recipe(key_name, ingredients_name, meal_name, prep_time):
    cookboock.update({key_name.lower(): {"ingredients": ingredients_name, "meal": meal_name.lower(), "prep_time": prep_time}})

# add_recipe(key_name, ingredients_name, meal_name, prep_time)

# --------------------------------------------------------------------------------
#command line executable

print(f"""{MAG}Welcome to the Python Cookbook !
      
                List of available option:
      
                1: Add a recipe
                2: Delete a recipe
                3: Print a recipe
                4: Print the cookbook
                5: Quit
      
                Please select an option:{RES}""")

number = input()


def main(number):

        if number == "1":

            key_name = input(f"{BLU}{BOL}Enter your own name of food for adding: {RES}")
            ingredients_name = list(map(str, (input(f"{BLU}{BOL}Enter all ingredients: {RES}").lower().split())))
            meal_name = input(f"{BLU}{BOL}Enter type of meal: {RES}")

            try:
                prep_time = int(input(f"{BLU}{BOL}Enter preperation time: {RES}"))
            except ValueError:
                print(f"{RED}{BOL}Enter number!{RES}")
                prep_time = int(input(f"{BLU}{BOL}Enter preperation time: {RES}"))

            add_recipe(key_name, ingredients_name, meal_name, prep_time)

        elif number == "2":

            name_of_food = input(f"{BLU}{BOL}Enter name of food for deletion: {RES}")
            delete_cook(name_of_food)

        elif number == "3":

            name_of_recipe = input(f"{CYA}{BOL}Enter name of food:{RES} ")
            print_recipe_details(name_of_recipe)

        elif number == "4":

            print_all_name_of_recipe(cookboock)

        elif number == "5":

            print(f"{YEL}Cookbook closed. Goodbye!{RES}")
        else:
            print(f"{RED}We don`t have a such options!{RES}")
        



main(number)