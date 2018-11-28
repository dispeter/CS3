import codecs 
import matplotlib.pyplot as plt
import pickle
movie_data = []
def get_movie_data():
    with codecs.open("load_movies.txt" , "r", encoding="utf-8") as f:
        # movie_data = []
        attributes = tuple(f.readline().strip().replace("\t", "").split(";"))
        # line = f.readlines()
        # attributes = line.strip().split(";")
        movie_data.append(list(attributes))

        f.readline()
        
        for line in f.readlines():
            line = line.replace("\t" , " ")
            line = line.strip().split(";")
            movie_data.append(tuple(line))
    return movie_data
movie_data = get_movie_data()       
# print(len(movie_data))


with codecs.open("load_movies.tsv" , "w" , encoding="utf-8") as f:
    for movie in movie_data:
        for item in movie:
            item = item.replace("\t" , "  ")
            f.write(item + "\t")
        f.write("\n")
movie_data = get_movie_data()
# print(movie_data)
# create_tsv(movie_data)

 # year, length, title ,subject,actor,actress,director,popularity,awards,image 
by_year = {}
by_actor = {}
by_female = {}
by_director = {}
by_length = {}
#sm dictionaries 
#By Year
for x in range(len(movie_data)):
    year = movie_data[x][0]
    by_year[year] = []
for i in range(len(movie_data)):
    if by_year[movie_data[i][0]] == "":
        by_year[movie_data[i][0]] = "N/A"
    by_year[movie_data[i][0]].append(movie_data[i])

#By length 
for x in range(len(movie_data)):
    length = movie_data[x][1]
    by_length[length] = []
for i in range(len(movie_data)):
    by_length[movie_data[i][1]].append(movie_data[i])

# #By Actor
for x in range(len(movie_data)):
    actor = movie_data[x][4]
    by_actor[actor] = []
for i in range(len(movie_data)):

    by_actor[movie_data[i][4]].append(movie_data[i])


#By Female 
for x in range(len(movie_data)):
    female = movie_data[x][5]
    by_female[female] = []
for i in range(len(movie_data)):

    by_female[movie_data[i][5]].append(movie_data[i])


# #By director 
for x in range(len(movie_data)):
    director = movie_data[x][6]
    by_director[director] = []
for i in range(len(movie_data)):

    by_director[movie_data[i][6]].append(movie_data[i])

#sm analysis 
average_length = []
# print(by_year)
def avg_year():
    for year in by_year:
        total_movielength = 0
        average_movie_length = 0
        for i in range(0,len(by_year[year])):
            if len(by_year[year][i][1]) > 0:
                total_movielength += int(by_year[year][i][1])
        average_movie_length = int(total_movielength/len(by_year[year]))
        average_length.append(average_movie_length)
        # print(average_movie_length)
            # average_length[by_year[i]] = average_movie_length
        # print("Average movie legnth in",year ,":", average_movie_length , "mins")
    with open("avgyear.pickle", "wb") as f:
        pickle.dump(average_length, f)
    with open('year.pickle', 'wb') as g:
        pickle.dump(by_year, g)

# Number of movies per year 
def movies_per_year():
    movie_per_year = []
    for year in by_year:
        # print("Number of movies in",year, ":",len(by_year[year]))
        movie_per_year.append(len(by_year[year]))
    # print(movie_per_year[0:])
    with open("movie_per_year.pickle", "wb") as f:
        pickle.dump(movie_per_year, f)

#pickkled cucumber be like

#by year
# with open("byyear.pickle", "wb") as f:
#     pickle.dump(by_year,f)

# with open("byyear.pickle", "wb") as f:
#     pickle.dump(by_year,f)

#by length
# with open("bylength.pickle", "wb") as f:
#     pickle.dump(by_length,f)

# with open("bylength.pickle", "rb") as f:
#     by_length = pickle.load(f)

#by actor
# with open("byactor.pickle", "wb") as f:
#     pickle.dump(by_actor,f)

# with open("byactor.pickle", "rb") as f:
#     by_actor = pickle.load(f)

#by female
# with open("byfemale.pickle", "wb") as f:
#     pickle.dump(by_female,f)

# with open("byfemale.pickle", "rb") as f:
#     by_female = pickle.load(f)

#by director
# with open("bydirector.pickle", "wb") as f:
#     pickle.dump(by_director,f)

# with open("bydirector.pickle", "rb") as f:
#     by_director = pickle.load(f)

avg_year()
# movies_per_year()