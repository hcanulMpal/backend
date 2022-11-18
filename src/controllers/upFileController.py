from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

class upFile():

    def uploadFile(self, data):
        print('llego aqui')

        load_dotenv()

        cloudinary.config(cloud_name = 'municipio-de-felipe-carrillo-puerto', api_key='939831556648318', api_secret= 'gpzkhczuJXhtXWv7ozmIBSzTLiQ')
        upload_result = None

        fileToUpload = data
        if fileToUpload:
            upload_result = cloudinary.uploader.upload(fileToUpload)
            print(upload_result)
            return jsonify(upload_result)

        

    