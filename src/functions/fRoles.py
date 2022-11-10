from ..models import db, Role

base = db.session

class functionRole:

    ROLES = ['SuperAdmin', 'Administrador', 'User']

    def is_Data(self):
        if not Role.query.all() :
            for item in self.ROLES:
                role = Role( name = item )
                base.add(role)
                base.commit()
            return True


    def setRoles(self):
        return roles_schema.jsonify(Role.query.all())


    def findUserRole(self, role):
        return Role.query.filter_by(name=role).first().id