# DOCKER

# Installing Docker on Ubuntu - go to official website (Docker docs)

# mkdir fapp2
# touch app.py

from flask import Flask
app=Flask(__name__)
@app.route('/')
def run():
    return "sanjith"
app.run('0.0.0.0',5000)
