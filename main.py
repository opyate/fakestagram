from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
import requests

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'img'
configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename
    return render_template('upload.html')

import requests
import shutil
import datetime as dt

from convert import convert

@app.route('/upload2', methods=['POST'])
def upload2():
    imgurl = request.get_data()

    r = requests.get(imgurl, stream=True)
    d = dt.datetime.now().isoformat()
    d = d.replace(':', '')
    path = 'img/{}.jpeg'.format(d)

    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

            convert(path)
            
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)