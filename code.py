# --------------
from csv import reader

def explore_data(dataset, start, end, rows_and_columns=False):
    for x in range(start,end):
      print (dataset[x])

def duplicate_and_unique_movies(dataset, index_):
    unique=[]
    duplicate=[]
    count=0
    for x in dataset:
      if x[index_] not in unique:
        unique.append(x[index_])
      elif x[index_] in unique:
        duplicate.append(x[index_])
    return duplicate    

def movies_lang(dataset, index_, lang_):
    movies_=[]
    for x in dataset:
        if x[index_]==lang_ and x not in movies_:
            movies_.append(x)
    return movies_
    explore_data(movies_,1,5)

def rate_bucket(dataset, rate_low):
    rated_movies=[]
    for x in dataset:
        if float(x[11])>=rate_low and x[13] not in rated_movies and x[3]=='en':
            rated_movies.append(x[13])
    return rated_movies
    explore_data(rated_movies,1,5)


# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)

#Remove header from the list and store it back in movies
del movies[0]

# The first row is header. Extract and store it in 'movies_header'.
movies_header=[]
for x in movies[0]:
  movies_header.append(x)

# Delete wrong data
# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
del movies[4553]

# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
explore_data(movies,0,5)

# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
duplicate_and_unique_movies(movies,13)
# We saw that there are 3 movies for which the there are multiple entries. 

# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
reviews_max={}
for x in movies:
  if x[13] not in reviews_max:
    reviews_max[x[13]]=x[12]
  elif x[13] in reviews_max and int(reviews_max[x[13]])<int(x[12]):
    reviews_max[x[13]]=x[12]

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean=[]
for x in movies:
  if x[13] not in movies_clean:
    movies_clean.append(reviews_max[x[13]])
    
# Calling movies_lang(), extract all the english movies and store it in movies_en.
movies_en=movies_lang(movies,3,'en')

# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies=rate_bucket(movies,8)
