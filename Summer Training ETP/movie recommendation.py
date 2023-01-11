#Dependencies
from matplotlib.pyplot import title
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Data Pre-processing

#loading csv file to pandas dataframe
movie_data = pd.read_csv('D:\Python for Geek\Chapter 1\movies.csv')
#printing first five rows of the dataframe

print(movie_data.head())
print(movie_data.shape)

#Selecting relevent featurs for recommendation
selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)
#replacing the null values with null string
for feature in selected_features:
    movie_data[feature] = movie_data[feature].fillna('')

#Combining all the 5 selected features
combined_features = movie_data['genres'] +' '+movie_data['keywords']+' '+movie_data['tagline']+' '+movie_data['cast']+' '+movie_data['director']
print(combined_features)

# Converting text data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
print(feature_vectors)

#Cosine Simalarity for getting similarity score
similarity = cosine_similarity(feature_vectors)
print(similarity)
print(similarity.shape)

#Getting movie name for the user
movie_name = input('Enter your favourite movie name: ')

#Create a list with all the movie names given in the dataset
list_of_all_titles = movie_data['title'].tolist()
print(list_of_all_titles)

#Finding the close match fo the name given by the user
find_close_match = difflib.get_close_matches(movie_name,list_of_all_titles)
print(find_close_match)
close_match = find_close_match[0]
print(close_match)

#Finding the index of the movie with with title
index_of_the_movie = movie_data[movie_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

#getting list of similar movies
similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

#length similaraity
print(len(similarity_score))

#sorting the movies based on their similarity scores
sorted_similar_movies = sorted(similarity_score,key = lambda x:x[1],reverse = True)
print(sorted_similar_movies)

#print the name of similar moives based on the index
print('Movies recommended for you: ')
i = 1
for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movie_data[movie_data.index == index]['title'].values[0]
    if(i<=10):
        print(i,'. ',title_from_index)
        i+=1 

#Movie recommendation system
