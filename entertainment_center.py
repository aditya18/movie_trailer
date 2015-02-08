import media
import fresh_tomatoes


toy_story = media.Movie("Toy",
                        "Toy Story is a 1995 American computer-animated buddy-comedy adventure film",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

                    
avatar = media.Movie("Avatar",
                     "Avatar is a 2009 American[9][10] epic science fiction film",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

batman = media.Movie("Batman Begins",
                     "Batman Begins is a 2005 superhero film based on the fictional DC Comics character Batman,",
                     "http://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                     "https://www.youtube.com/watch?v=vak9ZLfhGnQ")


avengers = media.Movie("Avengers",
                     "The Avengers is a 2012 American superhero film based on the Marvel Comics superhero team",
                     "http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                     "https://www.youtube.com/watch?v=zatgnqdIefs")

#print(avatar.storyline)
#avatar.show_trailer()

movies = [batman, avengers, toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)



