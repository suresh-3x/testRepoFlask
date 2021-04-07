import os
from os import listdir
from os.path import isfile, join
from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    return f"{file} saved succesfully."


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route("/gallery")
def get_gallery():
    target = os.path.join(APP_ROOT, 'images/')
    image_names = os.listdir(target)
    return render_template("gallery.html", image_names=image_names)

@app.route("/delete/<filename>")
def delete(filename):
    target = os.path.join(APP_ROOT, r'images\\' + filename)
    response = os.remove(target)
    print(target)
    print(response)
    return "File Deleteed Succesfully."

if __name__ == "__main__":
    app.run()
