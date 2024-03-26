from app import app
from flask import render_template

@app.route('/')
def index():
    photos = [
        {"url": "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759", "description": "Nature Scene"},
        {"url": "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759", "description": "Nature Scene"},
        {"url": "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759", "description": "Nature Scene"},
    ]
    return render_template("index.html", photos=photos)
