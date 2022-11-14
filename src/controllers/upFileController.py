from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api


class upFile():

    def uploadFile(self):

        app = Flask(__name__)
        app.logger.info('in upload route')

        load_dotenv()

        cloud_name = "municipio-de-felipe-carrillo-puerto" 
        api_key = "939831556648318" 
        api_secret = "gpzkhczuJXhtXWv7ozmIBSzTLiQ" 

        cloudinary.config(cloud_name = cloud_name, apy_key = api_key, api_secret = api_secret)


        if request.method == 'POST':
            fileToUpload = request.files['file']
            app.logger.info('% filoToUpload', fileToUpload)
            if fileToUpload:
                upload_result = cloudinary.uploader.upload(fileToUpload)
                app.logger.info(upload_result)
                return jsonify(upload_result)

        

    