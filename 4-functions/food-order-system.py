italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

def find_meal(name, menu):
  if name in menu:
    return name
  elif name not in menu:
    return None

def select_meal(name, food_type):
  if food_type == "Italian":
    return find_meal(name, italian_food)
  elif food_type == "Indian":
    return find_meal(name, indian_food)
  else:
    return None

def display_available_meals(food_type):
  if food_type == "Italian":
    print("Available Italian Meals: ")
    for food in italian_food:
      print(food)
  elif food_type == "Indian":
    print("Available Indian Meals: ")
    for food in indian_food:
      print(food)
  else:
    print("Invalid food type")

def create_summary(name, amount, food_type):
  order = select_meal(name, food_type)
  if order == name:
    return f"Your order: {amount} {name}"
  elif order == None:
    return "Meal not found"

print("Welcome to the Food Order System!")
type_input = input("Choose Meals (Italian/Indian): ")
display_available_meals(type_input)
name_input = input("Choose a Food: ")
amount_input = input("Order Quantity: ")
result = create_summary(name_input, amount_input, type_input)
print(result)
