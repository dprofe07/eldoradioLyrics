import flask
from flask import render_template

from eldoradioParser import eldoradio
import searchParser

app = flask.Flask(__name__)


@app.route('/')
def page_index():
    song = eldoradio.get_curr_song()
    return render_template('song_info.html', song=song)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)