import pickle
import matplotlib.pyplot as plt

Index=[]
Time=[]
X_axis_label=[]

with open('avgyear.pickle', 'rb') as f:
    average_movie_length = pickle.load(f)
with open('byyear.pickle', 'rb') as g:
    byyear = pickle.load(g)

for k in range(0,len(byyear)):
   Time.append(average_movie_length[byyear[k]])
   Index.append(k)
   if int(byyear[k]) % 10==0:
        X_axis_label.append(byyear[k])
   else:
        X_axis_label.append(' ')

fig, ax = plt.subplots()
bar_width = 0.5

rects1 = ax.bar(Index, Time, bar_width, color='b')

ax.set_xlabel('Year')
ax.set_ylabel('Length Of Movie In Minutes')
ax.set_title('Average Length Of Movies Per Year')
ax.set_xticks(Index)
ax.set_xticklabels(X_axis_label)

fig.tight_layout()
plt.show()
