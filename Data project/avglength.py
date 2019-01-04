import pickle
import matplotlib.pyplot as plt

with open('avgyear.pickle', 'rb') as f:
    average_movie_length = pickle.load(f)
with open('byyear.pickle', 'rb') as g:
    byyear = pickle.load(g)
avglength = []
index = []
x_axis = []
for i in range(0,len(byyear)):
    index.append(i)
    # if int(average_movie_length[i]) % 10 == 0:
    #     x_axis.append(byyear[i][1])
    # else: 
    #     x_axis.append(" ")

fig, ax = plt.subplots()
bar_width = 0.5


rects1 = ax.bar(average_movie_length, index, bar_width, color='b')


ax.set_xlabel('Year')
ax.set_ylabel('Length Of Movie In Minutes')
ax.set_title('Average Length Of Movies Per Year')
ax.set_xticks(index)
ax.set_xticklabels(x_axis)

fig.tight_layout()
plt.show()
