requested_toppings = ['mushrooms', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print("Sorry, we are out of mushrooms right now.")
    else:
        print(f"Adding {requested_topping}.")

requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("Hold the anchovies!")