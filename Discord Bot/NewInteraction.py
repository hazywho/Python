import numpy as np
import random
item = ["cat","fish","magnet","nothing"]
print(item)
secure_random = random.SystemRandom()
item = secure_random.choice(item)
print (item)