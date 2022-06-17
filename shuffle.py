from picker import SongPicker

catalog = {
    'Rock': ['Day Tripper', 'Icky Thump', 'Steady as She Goes', 'Tighten Up', 'Blue Orchid', 'Alas, Salvation', 'Boilermaker'],
    'Blues': ["I'm so Lonesome I could Cry", 'Folsom Prison Blues', 'Johnny B. Goode'],
    'MPB': ['Azul', 'Espera Pra Ver', 'Aquarela do Brasil', 'Fotografia', 'Baby', 'Mamãe Coragem'],
    'Rap': ['Goosebumps', 'Lalala', 'Sicko Mode', 'Suge', "God's Plan", 'Industry Baby']
}

def main():

    picker = SongPicker(catalog)
    song = picker.pick_song()
    print(song)

    genre,songs_list = picker.pick_genre()
    print(genre, songs_list)
    song = picker.pick_song_given_genre(genre)
    print(song)

    genre, song = picker.pick_song_and_genre()
    print(genre, song)

if __name__ == '__main__':
    main()
