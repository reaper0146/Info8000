#Soumya Pal
#Assignment 2 part 4

info = {
  "name": "Shomo Pal",
  "favorite_color": "Blue",
  "favorite_number": 10,
  "favorite_movies": ["Inception","The Shashank Redemption","One Piece (Anime not movie)"],
  "favorite_songs" : [{'artist': 'Metallica', 'title': 'Nothing Else Matters'}, 
         {'artist': 'Nirvana', 'title': 'Come as you are'}]
}

print(info["name"])
print(info["favorite_color"])
print(info["favorite_number"])
print("Movies:")
for movie_title in info["favorite_movies"]:
    print("\t"+ movie_title)
print("Songs:")
for song_info in info["favorite_songs"]:
    print(f"\t{song_info['artist']}: {song_info['title']}")