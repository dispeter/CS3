import matplotlib.pyplot as plt 
import pickle

with open("byyear.pickle", "rb") as f:
    by_year = pickle.load(f)

with open("Movie_Per_Year.pickle", "rb") as f:
    movie_per_year = pickle.load(f)
years = []
index = []
x_axis = []
no_of_movies = []
for i in range(0,len(by_year)):
    no_of_movies.append(movie_per_year[i])
    index.append(i)
for i in range(1920,2000):
    years.append(i)
    no = str(i)
    x_axis.append(no)


fig, ax = plt.subplots()
bar_width = 0.5

rects1 = ax.bar(index,no_of_movies , bar_width, color='b')


ax.set_xlabel('Year')
ax.set_ylabel('Number Of Movies per Year')
ax.set_title('Number of movies per year')
ax.set_xticks(index)
ax.set_xticklabels(years)

fig.tight_layout()
plt.show()