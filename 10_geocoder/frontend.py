from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from pathlib import Path

import backend

app = Flask(__name__)


@app.route('/')
def pre_submit():
    return render_template("pre_submit.html")


@app.route('/post_submit', methods=['POST'])
def post_submit():
    global local_filename
    if request.method == 'POST':
        file = request.files['file']
        local_filename = Path(secure_filename(f'uploaded_{file.filename}'))
        file.save(local_filename)
        if backend.add_lat_lon(local_filename):
            return render_template('post_submit.html')
        else:
            return render_template('pre_submit.html', text='Uploaded csv does not have an Address or address column.')


@app.route('/download_now')
def download():
    return send_file(local_filename, attachment_filename="download.csv", as_attachment=True, cache_timeout=0)


if __name__ == "__main__":
    app.run(debug=True)