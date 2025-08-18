#a city mapped by country

def city_country(city,country):
    '''function to map cities to countries'''
    cityname=f'"{city}, {country}"'

    return cityname.title()
city=city_country("nairobi","kenya")
print(city)


#album function

def make_album(music_name, artist):
    '''function making an album'''
    music={'author':artist, 'music':music_name}

    return music

album=make_album('iranda','joshua')
print(f" we have a new album details {album}")


#a function that allows users to enter artist and their music

def make_music(artist,music):
    '''function allowing users to nominate artists and their music'''
    print("please nominate your artist and their music")
    
    album1=f"{artist} {music}"

    return album1
while True:
    artist=input("name your artist  ")
    if artist == 'q':
        break

    music=input("what is their song  ")
    if music == 'q':
        break
    album1=f"{artist} {music}"
    mwiimbi=make_music(artist, music)
    print(mwiimbi)

