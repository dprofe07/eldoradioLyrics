import os

import flask
from flask import render_template

from eldoradioParser import eldoradio

if os.path.exists('/SERVER/is_server'):
    prefix = '/eldoradio-lyrics'
else:
    prefix = ''

app = flask.Flask(__name__, static_url_path=f'{prefix}/static')


@app.route(f'{prefix}/')
def page_index():
    song = eldoradio.get_curr_song()
    return render_template('song_info.html', song=song)


if __name__ == '__main__':
    app.run('127.0.0.1', 8007)

