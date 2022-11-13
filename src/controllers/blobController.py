from ..functions.functionBinary import Bloby
import requests

Bl = Bloby()

class BlobCtl:
    
    def setBlob(self, archivo):
        
        try: 
            toread = io.BytesIO(archivo)
            
        except ValueError as e:
            return jsonify({'data':e}),500

        return Bl.setBlob()
        
        
