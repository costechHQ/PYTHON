def city_country(city, country):
    """Returns a cleanly formatted string of city and country"""
    return f"{city.title()}, {country.title()}"

pair_1 = city_country("enugu", "nigeria")
pair_2 = city_country("Santiago", "chile")
pair_3 = city_country("cape_town", "south-africa")

print(pair_1)
print(pair_2)
print(pair_3)

print("\n" + "="*60 + "\n")

#8.7
def make_album(artist_name, album_title, songs=None):
    "Builds and returns a structure music album dictionary."
    album_dict = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }

    if songs:
        album_dict['songs'] = songs
    return album_dict

album_1 = make_album("daft punk", "random access memories")
album_2 = make_album("pink floyd", "the dark side the moon")
album_3 = make_album("taylor swift", "1989")

album_with_tracks = make_album("michael jackson", "thriller", songs=9)

print(album_1)
print(album_2)
print(album_3)
print(album_with_tracks)

print("\n" + "="*60 + "\n")

while True:
    artist_input = input("Artist name: ")
    if artist_input.lower() == 'q':
        break

    title_input = input("Album title: ")
    if title_input.lower() == 'q':
        break

    user_create_album = make_album(artist_input, title_input)
    print(f"\n Generated Dictionary object: {user_create_album}")

print("\n Thank you for using the Album Generate!")