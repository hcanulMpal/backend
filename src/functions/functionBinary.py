from ..models import db, Binary
from ..schemas.schemaBlob import Bl_Schema

base = db.session

class Bloby():

    def convertToBinaryData(self, filename):
        # Convercion del archivo a formato binario
        with open (filename, 'rb') as file:
            binaryData = file.read()
        return binaryData


    def insertBLOB(self, archivo):
        print("Insertar BLOB en la tabla binary")

        try:

            #Convertimos el archivo a formato binario
            binPhoto = archivo

            dbBinary = Binary(
                potho = binPhoto
            )
            base.add(dbBinary)
            base.commit()
        except Exception as error:
            print(error)


    def setBlob(self):
        return Bl_Schema.jsonify()


