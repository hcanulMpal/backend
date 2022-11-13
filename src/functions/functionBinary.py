from ..models import db, dbBinary

base = db.session

class Bloby():

    def convertToBinaryData(self, filename):
        # Convercion del archivo a formato binario
        with open (filename, 'rb') as file:
            binaryData = file.read()
        return binaryData


    def insertBLOB(self, filename):
        print("Insertar BLOB en la tabla binary")

        try:

            #Convertimos el archivo a formato binario
            binPhoto=self.convertToBinaryData(filename)

            dbBinary = dbBinary(
                potho = binPhoto
            )
            base.add(dbBinary)
            base.commit()
        except Exception as error:
            print(error)


