import searchParser


class Song:
    def __init__(self, name, artist, startTime, duration, image, sound):
        self.name = name
        self.artist = artist
        self.startTime = startTime
        self.duration = duration
        self.image = image
        self.sound = sound
        self.lyrics_url, self.lyrics = searchParser.find_on_azlyrics(f'{name.replace("&", "and")} {artist.replace("&", "and")}')
        if self.lyrics is None:
            self.lyrics_url, self.lyrics = searchParser.find_on_azlyrics(name.replace('&', 'and'))

    def formattedDuration(self):
        return f'{self.duration // 60} мин., {self.duration % 60} сек.'

    @classmethod
    def from_dict(cls, dct):
        try:
            if dct['info'] is None:
                dct['info'] = {
                    'song': dct['song'].capitalize(),
                    'artistsName': dct['artist'].capitalize(),
                    'image': 'about:blank',
                    'audio': 'about:blank'
                }
            return cls(
                dct['info']['song'],
                dct['info']['artistsName'],
                dct['startTime'],
                dct['duration'],
                dct['info']['image'],
                dct['info']['audio']
            )
        except TypeError:
            print(dct)
            raise