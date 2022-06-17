import pytest

from picker import SongPicker

catalog = {
    'Rock': ['Day Tripper', 'Icky Thump', 'Steady as She Goes', 'Tighten Up', 'Blue Orchid', 'Alas, Salvation', 'Boilermaker'],
    'Blues': ["I'm so Lonesome I could Cry", 'Folsom Prison Blues', 'Johnny B. Goode'],
    'MPB': ['Azul', 'Espera Pra Ver', 'Aquarela do Brasil', 'Fotografia', 'Baby', 'Mamãe Coragem'],
    'Rap': ['Goosebumps', 'Lalala', 'Sicko Mode', 'Suge', "God's Plan", 'Industry Baby']
}

class TestSongPicker:

    def test_pick_a_song(self):
        picker = SongPicker(catalog)
        song = picker.pick_song()

        assert song in ['Day Tripper', 'Icky Thump', 'Steady as She Goes',
                'Tighten Up', 'Blue Orchid', 'Alas, Salvation', 'Boilermaker',
                "I'm so Lonesome I could Cry", 'Folsom Prison Blues', 'Johnny B. Goode',
                'Azul', 'Espera Pra Ver', 'Aquarela do Brasil',
                'Fotografia', 'Baby', 'Mamãe Coragem', 'Goosebumps', 'Lalala',
                'Sicko Mode', 'Suge', "God's Plan", 'Industry Baby']

    def test_pick_a_genre(self):
        picker = SongPicker(catalog)
        genre,songs_list = picker.pick_genre()

        assert genre in ['Rock', 'Blues', 'MPB', 'Rap']

    def test_pick_a_song_given_a_genre(self):
        picker = SongPicker(catalog)
        song = picker.pick_song_given_genre('Blues')

        assert song in ["I'm so Lonesome I could Cry", 'Folsom Prison Blues',
                'Johnny B. Goode']

    def test_cannot_pick_song_for_unavailable_genre(self):
        picker = SongPicker(catalog)
        with pytest.raises(Exception) as e:
            song = picker.pick_song_given_genre('Pop')

    def test_pick_a_song_and_a_genre(self):
        picker = SongPicker(catalog)
        genre, song = picker.pick_song_and_genre()

        assert song in ['Day Tripper', 'Icky Thump', 'Steady as She Goes',
                'Tighten Up', 'Blue Orchid', 'Alas, Salvation', 'Boilermaker',
                "I'm so Lonesome I could Cry", 'Folsom Prison Blues', 'Johnny B. Goode',
                'Azul', 'Espera Pra Ver', 'Aquarela do Brasil',
                'Fotografia', 'Baby', 'Mamãe Coragem', 'Goosebumps', 'Lalala',
                'Sicko Mode', 'Suge', "God's Plan", 'Industry Baby']

        assert genre in ['Rock', 'Blues', 'MPB', 'Rap']
