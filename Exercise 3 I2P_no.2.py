
def calc_weight_on_planet(weight, gravity = 23.1):
    earth_gravity = 9.8
    mass = weight/earth_gravity
    weight_on_planet = mass*gravity
    print(weight_on_planet)


calc_weight_on_planet(78,9.8)