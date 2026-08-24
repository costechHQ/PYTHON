def make_sandwich(*toppings):
    """Summerizes a sandwich order with arbitrary toppings."""
    print("\n Making a delicous sandwich with the following items:")
    for topping in toppings:
        print(f" - {topping}")

make_sandwich("roast beef", "chedder cheese", "lettuce")
make_sandwich("turkey", "swiss cheese")
make_sandwich("peanut butter", "jelly", "banna slices", "honey")

print("\n" + "="*40 + "\n")

#8.13

def build_profile(first, last, **user_info):
    """BUilds a comprehensive dictionary containing everything we know about a user."""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

my_profile = build_profile(
    first="artificial",
    last="intelligence",
    field="Computer Science",
    role="Adaptive AI Collaborator",
    hobby="Analyzing Python code"
)

print(my_profile)

print("\n" + "="*40 + "\n")

def make_car(manufacturer, model, **car_features):
    """Stores required vehicle metrics along with optional properties inside a dictionary."""
    car_features['manufacturer'] = model.title()
    return car_features

car_data = make_car(
    'subaru',
    'outback',
    color='blue',
    tow_package=True
)

print(car_data)