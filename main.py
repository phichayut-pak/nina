import os
# example of recipe in txt
# ID;Name;Ingredient1|Ingredient2|...;Instruction1|Instruction2|...;Calories

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# * * Load the file and Returns as List
def load(filename):
    try:
        with open(filename, 'r') as file:
            recipes = file.readlines() 
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        recipes = []
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
        recipes = []

    return recipes

# * * Overwrite the file
def save(filename, recipes): #recipes are the whole recipes
    try:
        with open(filename, 'w') as file:
            file.writelines(recipes) 
    except IOError:
        print(f"Error: Unable to write to file '{filename}'.")

# example of recipe:

# 'name': 'Smoothie',
# 'ingredients': ['Banana', 'Yogurt', 'Honey'],
# 'instructions': ['Blend all ingredients', 'Serve chilled'],
# 'calories': 250

def add_recipe(filename, name, ingredients, instructions, calories):
    recipes = load(filename)

    if recipes:
        last_id = 0
        for recipe in recipes:
            recipe_parts = recipe.strip().split(";")
            current_id = int(recipe_parts[0])
            if(current_id > last_id):
                last_id = current_id

    else:
        last_id = 0

    new_id = last_id + 1

    ingredients_str = '|'.join(ingredients)
    instructions_str = '|'.join(instructions)

    new_recipe = f"{new_id};{name};{ingredients_str};{instructions_str};{calories}"

    try:
        with open(filename, 'a') as file:
            file.write(new_recipe)
        
        print(f"Recipe '{name}' added with ID {new_id}")
    
    except IOError:
        print(f"Error: Unable to write to file '{filename}'.")


# Update by ID
def update_recipe(filename, recipe_id, new_name, new_ingredients, new_instructions, new_calories):
    recipes = load(filename)
    updated = False

    for index, recipe in enumerate(recipes):
        recipe_data = recipe.strip().split(";")
        if int(recipe_data[0]) == int(recipe_id):
            ingredients_str = '|'.join(new_ingredients)
            instructions_str = '|'.join(new_instructions)
            recipes[index] = f"{recipe_id};{new_name};{ingredients_str};{instructions_str};{new_calories}"
            updated = True
            break

    if updated:
        save(filename, recipes)
        print(f"Recipe with ID {recipe_id} updated successfully.")
    else:
        print(f"Error: Recipe with ID: {recipe_id} not found.")

# Delete by ID
def delete_recipe(filename, recipe_id):
    recipes = load(filename)
    initial_count = len(recipes)

    new_recipes = []
    
    for recipe in recipes:
        recipe_parts = recipe.split(";")

        if int(recipe_parts[0]) != recipe_id:
            new_recipes.append(recipe)

    if len(recipes) < initial_count:
        save(filename, new_recipes)
        print(f"Recipe with ID {recipe_id} deleted successfully.")
    else:
        print(f"Error: Recipe with ID {recipe_id} not found.")



# 1. Pancakes
# - Ingredients
#       - Flour
#       - Egg
# - Instructions
#       1. Mix ingredients
#       2. Cook on pan
# - Calories: 350       

def display_recipes(filename):
    recipes = load(filename)
    print("========================================================================\n")
    for recipe in recipes:
        recipe = recipe.strip().split(";")
        recipe_id = recipe[0]
        name = recipe[1]
        ingredients = recipe[2].split("|")
        instructions = recipe[3].split("|")
        calories = int(recipe[4])

        print(f"{recipe_id}. {name}")
        print("- Ingredients")

        for ingredient in ingredients:
            print(f"     - {ingredient}")
            
        print("- Instructions")
        
        for index, instruction in enumerate(instructions, start=1):
            print(f"        {index}. {instruction}")

        print(f"- Calories: {calories}\n")
        print("========================================================================\n")


def filter_by_calories(filename, max_calories):
    recipes = load(filename)

    filtered_recipes = list(filter(
        lambda recipe: int(recipe.strip().split(';')[4]) <= max_calories if len(recipe.strip().split(';')) == 5 else False,
        recipes
    ))

    if(filtered_recipes == []):
        print(f"\nRecipes with Calories <= {max_calories} Not Found.")
        return

    print(f"\nRecipes with Calories <= {max_calories}:")
    for recipe in filtered_recipes:
        recipe_parts = recipe.strip().split(';')
        
        # Extract recipe details
        recipe_id = recipe_parts[0]
        name = recipe_parts[1]
        ingredients = recipe_parts[2].split('|')
        instructions = recipe_parts[3].split('|')
        calories = recipe_parts[4]
        
        # Display recipe in the specified format
        print(f"{recipe_id}. {name}")
        print(f"- Ingredients")
        for ingredient in ingredients:
            print(f"      - {ingredient}")
        print(f"- Instructions")
        for i, instruction in enumerate(instructions, start=1):
            print(f"      {i}. {instruction}")
        print(f"- Calories: {calories}\n")
    



WELCOME_ART = """
██████╗ ███████╗ ██████╗██╗██████╗ ███████╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔════╝    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██████╔╝█████╗  ██║     ██║██████╔╝█████╗      ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██╔══██╗██╔══╝  ██║     ██║██╔═══╝ ██╔══╝      ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║  ██║███████╗╚██████╗██║██║     ███████╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝     ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                                     
"""

DISPLAY_ART = """
██████╗ ███████╗ ██████╗██╗██████╗ ███████╗███████╗
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔════╝██╔════╝
██████╔╝█████╗  ██║     ██║██████╔╝█████╗  ███████╗
██╔══██╗██╔══╝  ██║     ██║██╔═══╝ ██╔══╝  ╚════██║
██║  ██║███████╗╚██████╗██║██║     ███████╗███████║
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝     ╚══════╝╚══════╝
"""



def main():
    filename = "recipes.txt"
    clear_screen()
    print(WELCOME_ART)  # Print the ASCII welcome art
    print("Welcome to the Recipe Manager!")
    
    while True:
        print("\nPlease select an option:")
        print("1. Add a new recipe")
        print("2. Update a recipe by ID")
        print("3. Delete a recipe by ID")
        print("4. Display all recipes")
        print("5. Filter recipes by calories")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        clear_screen()
        
        match choice:
            case '1':
                name = input("Enter the recipe name: ")
                ingredients = input("Enter ingredients (separated by commas): ").split(", ")
                instructions = input("Enter instructions (separated by commas): ").split(", ")
                calories = input("Enter calories: ")
                add_recipe(filename, name, ingredients, instructions, calories)
            
            case '2':
                recipe_id = int(input("Enter the recipe ID to update: "))
                new_name = input("Enter the new name: ")
                new_ingredients = input("Enter new ingredients (separated by commas): ").split(", ")
                new_instructions = input("Enter new instructions (separated by commas): ").split(", ")
                new_calories = input("Enter new calories: ")
                update_recipe(filename, recipe_id, new_name, new_ingredients, new_instructions, new_calories)
            
            case '3':
                recipe_id = int(input("Enter the recipe ID to delete: "))
                delete_recipe(filename, recipe_id)
            
            case '4':
                print(DISPLAY_ART)
                display_recipes(filename)
            
            case '5':
                max_calories = int(input("Enter the maximum calories: "))
                filter_by_calories(filename, max_calories)
            
            case '6':
                print("Thank you for using the Recipe Manager. Goodbye!")
                break
            
            case _:
                print("Invalid choice. Please try again.")

        input("\nPress Enter to return to the main menu...")
        clear_screen()

# Run the main program
if __name__ == "__main__":
    main()
