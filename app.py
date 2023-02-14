import flask
from flask import render_template

from eldoradioParser import eldoradio

app = flask.Flask(__name__)


@app.route('/')
def page_index():
    song = eldoradio.get_curr_song()
    return render_template('song_info.html', song=song)


if __name__ == '__main__':
    app.run('127.0.0.1', 8007)

