import random
chamber_positon = 1
bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    spin_chamber()
    if chamber_position == 3:
        return "You are dead!"
    else: 
        return "Keep playing"


print(fire_gun)