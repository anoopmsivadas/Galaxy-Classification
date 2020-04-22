from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import classifier


UPLOAD_FOLDER = './static/upload/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    result, filename = '',''
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = classifier.predict_galaxy(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    return render_template("index.html", result=result,path=os.path.join(app.config['UPLOAD_FOLDER'], filename) )


if __name__ == "__main__":
    app.run(debug=True)  
