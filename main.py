import pygame
# from flask import *
# from werkzeug.utils import secure_filename
# from markupsafe import escape
from time import sleep

path_to_app = '/home/pi/wantAlarm/'

def alarm():
    # start the music
    file = path_to_app + 'changes.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

alarm()
sleep(10)

# app = Flask(__name__)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['the_file']
#         file.save(f"{secure_filename(file.filename)}")

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"


 