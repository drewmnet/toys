from random import random as rnd

def roll(dice):
    return int(rnd() * dice) + 1
    
message = "Purple Turkey, Purple Turkey, this is Red Snail. Do you copy? Over."
signal_strength = 99 # percent
final_string = ""

for i in range(len(message)):
    r = roll(100)
    if r <= signal_strength:
        final_string += message[i:i+1]
    else:
        final_string += "*"
        
print(final_string)
