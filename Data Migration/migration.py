import codecs 
import matplotlib.pyplot as plt
import pickle
migrate = []
def get_movie_data():
    with codecs.open("migration.txt" , "r", encoding="utf-8") as f:
        # movie_data = []
        attributes = tuple(f.readline().strip().replace("\t", "").split(";"))
        # line = f.readlines()
        # attributes = line.strip().split(";")
        migrate.append(list(attributes))

        f.readline()
        
        for line in f.readlines():
            line = line.replace("\t" , " ")
            line = line.strip().split(";")
            migrate.append(tuple(line))
    return migrate
migrate = get_movie_data()       
# print(len(movie_data))


with codecs.open("migration.tsv" , "w" , encoding="utf-8") as f:
    for movie in migrate:
        for item in movie:
            item = item.replace("\t" , "  ")
            f.write(item + "\t")
        f.write("\n")
movie_data = get_movie_data()