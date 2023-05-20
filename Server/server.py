#!/usr/bin/env

from flask import Flask, redirect, url_for, render_template, send_file, request
from werkzeug.utils import secure_filename
import config as CONFIG
import helper

# Flask app configuration

app = Flask(__name__)
app.config.update(
    SECRET_KEY = CONFIG.SECRET_KEY
)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/uploader', methods = ['GET', 'POST'])
def handle_upload_file():
   if request.method == 'POST':
      
        if 'file' not in request.files:
            return redirect(request.url)

        f = request.files['file']

        if f.filename == '':
            return redirect(request.url)
      
        if f and helper.allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(filename)
            return 'file uploaded successfully'

@app.route('/Files/<name>')
def handle_download_file(name):
    return send_file(name, as_attachment=True)

@app.route('/')
def main():
   return render_template('index.html'), 200

@app.route("/about",methods=["GET", "POST"])
def handle_about_page():
    pass

@app.route("/contact",methods=["GET", "POST"])
def handle_contact_page():
    pass

@app.route("/privacy",methods=["GET", "POST"])
def handle_term_and_privacy_page():
    pass

@app.route("/blog/<id>",methods=["GET", "POST"])
def handle_blog_page(id):
    pass

@app.route("/admin",methods=["GET", "POST"])
def handle_admin_page():
    pass

if __name__ == "__main__":
    app.run(CONFIG.HOST,CONFIG.RUNNING_PORT,debug=CONFIG.DEBUG_MODE)