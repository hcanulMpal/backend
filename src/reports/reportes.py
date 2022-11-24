from flask import current_app, send_file
import os

class Mapa():

    def mapa(self):
        path = current_app.config['STATIC_FOLDER_DOC']
        pdfs = os.path.join(path,'mapaTuristico.pdf')
        return send_file(pdfs, download_name= "mapaTuristico.pdf", as_attachment=True)
