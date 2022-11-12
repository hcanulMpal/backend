from ..models import db, Category

base = db.session

class funcCat:
    
    cat = ['Arte', 'Cultura', 'Entretenimiento', 'Accidente', 'Economia', 'Politica', 'Salud', 'Sociedad', 'Presidencia']

    def is_Data(self):
        if not Category.query.all():
            for item in self.cat:
                category = Category( category = item )
                base.add(category)
                base.commit()
            return True

    
    def findNoticesCategory(self, cate):
        return Category.query.filter_by(category=cate).first().id