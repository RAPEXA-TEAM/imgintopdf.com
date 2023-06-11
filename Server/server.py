#!/usr/bin/env

from flask import Flask, redirect, url_for, render_template, send_file, request, jsonify
from werkzeug.utils import secure_filename
import os
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

@app.route("/tool",methods=["GET", "POST"])
def handle_tool_page():
    
    if request.method == 'POST':
      
        if 'file' not in request.files:
            print(401)

        f = request.files['file']
        output = request.form.getlist('output')

        if output == []:
            output = ['off']

        if f.filename == '':
            print(401)
      
        if f and helper.allowed_file(f.filename):
            
            filename = secure_filename(f.filename)
            filepath = os.path.join(CONFIG.UPLOADS_PATH, filename)
            f.save(filepath)
            fname = helper.make_pdf_from_selected_files([filepath])

            if output == ['on']:

                zippath = os.path.join(CONFIG.UPLOADS_PATH, f"{fname}.zip")

                return send_file(zippath, as_attachment=True), 200

            pdfpath = os.path.join(CONFIG.UPLOADS_PATH, f"{fname}.pdf")

            return send_file(pdfpath, as_attachment=True), 200
        
        return render_template("tool.html"), 200
       
    return render_template('tool.html'), 200

@app.route('/')
def main():
   return render_template('index.html'), 200

@app.route("/about",methods=["GET", "POST"])
def handle_about_page():
    return render_template('about.html'), 200

@app.route("/contact",methods=["GET", "POST"])
def handle_contact_page():
    return render_template('contact.html'), 200

@app.route("/privacy",methods=["GET", "POST"])
def handle_term_and_privacy_page():
    return render_template('privacy.html'), 200

@app.route("/blog",methods=["GET", "POST"])
def handle_blog_page():
    return render_template('blog.html'), 200

@app.route("/blog/<id>",methods=["GET", "POST"])
def handle_blog_post_page(id):
    return render_template('blog.html'), 200

@app.route("/admin",methods=["GET", "POST"])
def handle_admin_page():
    pass

if __name__ == "__main__":
    app.run(CONFIG.HOST,CONFIG.RUNNING_PORT,debug=CONFIG.DEBUG_MODE)