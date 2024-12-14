import pygame
from flask import *
from werkzeug.utils import secure_filename
from markupsafe import escape

def alarm():
    # start the music
    file = 'changes.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"{secure_filename(file.filename)}")

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"





