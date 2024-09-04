spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
print(spicy_foods)
def get_names(spicy_foods):
    names_of_food =[item["name"] for item in spicy_foods]
    return names_of_food
    pass

print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    spicy_5 = [item for item in spicy_foods if item["heat_level"]>5]
    return spicy_5

    pass

print(get_spiciest_foods(spicy_foods))
def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        emojis = "🌶"*item["heat_level"]
        print(f'{item["name"]} ({item["cuisine"]}) | Heat Level: {emojis}')
    pass

print(print_spicy_foods(spicy_foods))
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item["cuisine"]== cuisine:
            return item
    pass
print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item["heat_level"] > 5:
            emojis = "🌶"*item["heat_level"]
            print(f'{item["name"]} ({item["cuisine"]}) | Heat Level: {emojis}')
    pass
print(print_spiciest_foods(spicy_foods))
def get_average_heat_level(spicy_foods):
    total=0
    for item in spicy_foods:
        total = total + item["heat_level"]
        average = total/len(spicy_foods)
    return average 
    pass
print(get_average_heat_level(spicy_foods))


spicy_food =  {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
print(create_spicy_food(spicy_foods, spicy_food))