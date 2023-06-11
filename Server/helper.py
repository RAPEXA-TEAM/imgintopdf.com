from PIL import Image
import random
import string
import zipfile
import config
import os

def generate_random_file_name():

    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(12))
    return result_str

def make_pdf_from_selected_files(selected_files):

    filename = generate_random_file_name()
    
    images_list = []
    
    for f in selected_files:

        images_list.append((Image.open(f)).convert('RGB'))

    pdfpath = os.path.join(config.UPLOADS_PATH, f"{filename}.pdf")

    images_list[0].save(pdfpath, save_all=True, append_images=images_list[1:])
    
    zippath = os.path.join(config.UPLOADS_PATH, f"{filename}.zip")

    with zipfile.ZipFile(zippath , mode="w") as archive:
        archive.write(pdfpath)

    return filename

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS