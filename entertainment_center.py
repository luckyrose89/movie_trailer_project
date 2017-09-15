import fresh_tomatoes
import media
import imdb


print("Fetching Movie info from the API, Please Wait for 70 seconds...")

youtube_prepend = 'https://www.youtube.com/watch?v='
my_movies_list = []
imdb_data = imdb.IMDb()

#Function to convert unicode data to string in a list
def list_filter(list_arg):
    list_arg = [str(index) for index in list_arg]
    list_arg = ', '.join(list_arg)
    return list_arg

#Dictionary to store IMDb movie Id and trailer links in separate keys
movies_dict = {
        'Toy Story': {'id': '0114709', 'trailer':'KYz2wyBy3kc'},
        'avatar': {'id':'0499549', 'trailer':'5PSNL1qE6VY'},
        'the_avengers': {'id':'0848228', 'trailer':'hIR8Ar-Z4hw'},
        'i_robot': {'id':'0343818', 'trailer':'s0f3JeDVeEo'},
        'empire_of_the_sun': {'id':'0092965', 'trailer':'i_WiDVA1kLY'},
        'lord_of_the_rings':{'id':'0120737', 'trailer': 'V75dMMIW2B4'},
        'goodwill_hunting':{'id':'0119217', 'trailer': 'QSMvyuEeIyw'},
        'theory_of_everything':{'id':'2980516', 'trailer': 'Salz7uGp72c'},
        'contact':{'id':'0118884', 'trailer': 'SRoj3jK37Vc'}
    }


#Loop to iterate over movie keys to create instances of Movie class
for x in movies_dict:
    movieKeys = movies_dict[x].values()
    movie_data = imdb_data.get_movie(movieKeys[0])
    movie_trailer = youtube_prepend+movieKeys[1]
    genre_list = movie_data['genres']
    genre_list = list_filter(genre_list)
    movie = media.Movie(movie_data['title'],genre_list, movie_data['rating'], movie_data['plot outline'], movie_data['cover url'], movie_trailer)
    my_movies_list.append(movie)
                        
    
        
    

fresh_tomatoes.open_movies_page(my_movies_list)



