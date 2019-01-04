import matplotlib.pyplot as plt 

susceptible = 0.99
infected = 0.01
recovered = 0
beta = 0.016 #Rate at which people move from susceptible to infected
gamma = 0.001 #Rate at which people move from infected to recovered
steps = 100 
graph_susceptible = []
graph_infected = []
graph_recovered = []
graph_steps = []
for i in range(0,365):
    new_infected = beta * infected * susceptible
    new_recovered = gamma * infected

    susceptible -= new_infected
    infected +=(new_infected - new_recovered)
    recovered += new_recovered
    graph_infected.append(infected)
    graph_susceptible.append(susceptible)
    graph_recovered.append(recovered)
    graph_steps.append(i)


plt.figure()
plt.plot(graph_steps, graph_susceptible, label='Susceptible')
plt.plot(graph_steps, graph_recovered, label='Recovered')
plt.plot(graph_steps, graph_infected, label='Infected')

#Create a label for each plot

plt.legend(['Susceptible', 'Infected', 'Recovered', 'Dead'], loc='upper right')
plt.xlabel('Number of Days')
plt.ylabel('Population%')
plt.title('SIRs')

plt.show()