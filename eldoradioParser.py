import time

import socketio

from song import Song


class EldoRadio:
    def __init__(self):
        self.client = socketio.Client(logger=True, engineio_logger=True)
        self.client.connect('https://mplb.emg.fm/', namespaces=['/eldo'])
        self._song = None

        @self.client.on('playlist', namespace='/eldo')
        def upd_playlist(data):
            self._song = Song.from_dict(data[0])

        @self.client.on('song began', namespace='/eldo')
        def song_began(data):
            self._song = Song.from_dict(data)

    def get_curr_song(self):
        if self._song is None:
            self.client.emit('get playlist', 1, namespace='/eldo')
            while self._song is None:
                time.sleep(0.1)

        return self._song


eldoradio = EldoRadio()
