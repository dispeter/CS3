import matplotlib.pyplot as plt

S = 0.999
I = 0.001
R = 0
dead = 0

beta = 0.2
# Rate at which people move from susceptible to infected
gamma = 0.0005
# Rate at which people move from infected to recovered
steps = 100
death_rate = 0.02

# Lists
graph_S = []
graph_I = []
graph_R = []
graph_D = []
graph_steps = []

for tick in range(steps):
    new_infected = S * I * beta
    new_recovered = gamma * I
    new_dead = death_rate * I

    S -= new_infected
    I += (new_infected - new_recovered - new_dead)
    R += new_recovered
    dead += new_dead

    # print(S + I + R + dead)

    graph_steps.append(tick)
    graph_S.append(S)
    graph_I.append(I)
    graph_R.append(R)
    graph_D.append(dead)


def simulation_view():
    fig_size = plt.rcParams["figure.figsize"]

    fig_size[0] = 15
    fig_size[1] = 6
    plt.rcParams["figure.figsize"] = fig_size


simulation_view()

plt.figure()
plt.plot(graph_steps, graph_S)
plt.plot(graph_steps, graph_I)
plt.plot(graph_steps, graph_R)
plt.plot(graph_steps, graph_D)

plt.legend(['Susceptible', 'Infected', 'Recovered', 'Dead'], loc='upper right')
plt.xlabel('Days')
plt.ylabel('Fraction of the Population')
plt.title('SIR Model')

plt.show()