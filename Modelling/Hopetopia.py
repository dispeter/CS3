from random import randint, triangular, random
import matplotlib.pyplot as plt
import math

steps = 12 
male = 84
female = 91 
abletohavechild = 0.6
actuallychild = abletohavechild * 0.3 
death_rate = 0.05 
starvation_rate = 0.01
current_starvation_rate = starvation_rate
predator = 0.1
x_coords = []
y_coords = []
for i in range(0,100):
    current_starvation_rate = starvation_rate * math.log((male+female),10)
    random_function = random() 
    male -= int(male * death_rate)
    female -= int(female * death_rate)
    if (male+female) > 1000:
        male -= int(male * predator)
        female -= int(female * predator)
    male -= int(male * starvation_rate)
    female -= int(female * starvation_rate)
    for x in range(0,male+female):
        if random() <= actuallychild:
            if random_function <= 0.5: 
                male += 1
            else:
                female +=1 
    x_coords.append(i)
    y_coords.append(male + female)
plt.figure()
plt.plot(x_coords, y_coords)
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Hopetopia Population Growth")
plt.show()