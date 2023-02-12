import searchParser

a = {
    'song': 'ROAD TRIPPIN',
    'artist': 'RED HOT CHILI PEPPERS',
    'startTs': 1676198450,
    'startTime': '13:40:50',
    'duration': 204,
    'info': {'song': 'Road Trippin', 'artistsName': 'Red Hot Chili Peppers',
                              'image': 'https://performer.emg.fm/thumb/api_300x300/songs/2017/71/6144591f056dd06f3_1024x1024bb.jpg',
                              'audio': 'https://performer.emg.fm/upload/songs/hook/2017/3e/38ff/591f056dd6601.mp3',
                              'duration': '00:00:00',
                              'artists': [{'id': '768', 'name': 'Red Hot Chili Peppers', 'prefix': ''}]}}

class Song:
    def __init__(self, name, artist, startTime, duration, image, sound):
        self.name = name
        self.artist = artist
        self.startTime = startTime
        self.duration = duration
        self.image = image
        self.sound = sound
        self.lyrics_url, self.lyrics = searchParser.find_on_azlyrics(f'{name.replace("&", "and")} {artist.replace("&", "and")}')

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