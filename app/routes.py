from flask import render_template, request,redirect,url_for
import requests
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_id = request.form.get('video_id')
        return redirect(url_for('show_thumbnail', video_id=video_id))
    return render_template("index.html")

@app.route('/show_thumbnail/<video_id>')
def show_thumbnail(video_id):
    thumbnail_url = f"http://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return render_template("images.html", thumbnail_url=thumbnail_url)
