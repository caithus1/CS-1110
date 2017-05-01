# Christopher Geier (cpg3rb)
import random

restaurants = ["Sticks", "Yuan Ho", "Melting Pot", "East Garden"]
styles = ["Casual", "Chinese", "Fancy", "Chinese"]
costs = ["$", "$", "$$$", "$$"]


def get_random_restaurant():
    index = random.randint(0,3)
    return restaurants[index],styles[index],costs[index]


def get_restaurant_style(chosen_style):
    possible_choices = []
    for i in range(len(styles)):
        if chosen_style == styles[i]:
            possible_choices.append(i)
    choice_index = random.choice(possible_choices)
    return restaurants[choice_index], chosen_style, costs[choice_index]


def get_restaurant_cost(chosen_cost):
    possible_choices = []
    for i in range(len(costs)):
        if chosen_cost == costs[i]:
            possible_choices.append(i)
    choice_index = random.choice(possible_choices)
    return restaurants[choice_index], styles[choice_index], chosen_cost


print("Welcome to WahooSpoon!")
print("  1. Get a random restaurant")
print("  2. Get a random restaurant based on style")
print("  3. Get a random restaurant based on cost")
choice = int(input("Choice? "))
if choice == 1:
    r, s, c = get_random_restaurant()
elif choice == 2:
    print(set(styles))
    style = input("What style would you like?: ")
    r, s, c = get_restaurant_style(style)
else:
    print(set(costs))
    cost = input("What cost would you like?: ")
    r, s, c = get_restaurant_cost(cost)

print("We're going to", r, "today! (Style:", s, "/ Cost:", c, ")")
