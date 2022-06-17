import random

class SongPicker():

    def __init__(self, catalog):
        self.catalog = catalog

    def pick_song(self):
        selected = random.choice(list(self.catalog.items()))
        songs_list = selected[1]
        song = random.choice(songs_list)

        return song

    def pick_song_given_genre(self, genre):
        songs_list = self.catalog[genre]
        song = random.choice(songs_list)

        return song

    def pick_genre(self):
        selected = random.choice(list(self.catalog.items()))
        genre = selected[0]
        songs_list = selected[1]

        return genre, songs_list

    def pick_song_and_genre(self):
        selected = random.choice(list(self.catalog.items()))
        genre = selected[0]
        songs_list = selected[1]
        song = random.choice(songs_list)

        return genre, song

