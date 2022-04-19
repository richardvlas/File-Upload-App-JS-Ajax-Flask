from app import app
from flask import request, render_template, jsonify, make_response


@app.route("/")
def index():
    return 'HELLO'


@app.route('/upload-video', methods=['GET', 'POST'])
def upload_video():

    print(request.method)

    if request.method == 'POST':

        filesize = request.cookies.get('filesize')
        file = request.files["file"]

        print(f"Filesize: {filesize}")
        print(file)

        res = make_response(jsonify({"message": f"{file.filename} uploaded"}), 200)

        return res


    return render_template('public/upload_video.html')

