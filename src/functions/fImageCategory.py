from ..models import db, ImgCategory

base = db.session

class dbImgCat:
    cat = ['Carrusel_1', 'Carrusel_2', 'Avisos', 'Noticias', 'Turismo_Galery', 'Cultura']

    def is_Data(self):
        if not ImgCategory.query.all():
            for item in self.cat:
                category = ImgCategory( categorys = item)
                base.add(category)
                base.commit()

    
    def findImageCategory(self, data):
        return ImgCategory.query.filter_by(categorys=data).first().id