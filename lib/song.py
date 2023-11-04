class Song:
    
    count = 0
    songs = []
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_artists(self.artist)
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)
       
   
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
      

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
       
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)  # Always add the genre
        
        # # Remove duplicates by converting to a set and back to a list
        # cls.genres = list(set(cls.genres))
        
    
    @classmethod
    def add_to_genre_count(cls, genre):
       cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
       cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1


    





