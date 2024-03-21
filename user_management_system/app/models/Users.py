from instance import db,app


class User(db.Model):
    #__table_args__ = {"schema":"app_authentication"}
    __tablename__ = "user_details"

    user_id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100))
    login_id = db.Column(db.String(100), unique=True, nullable = False)
    country = db.Column(db.String(100))
    department = db.Column(db.String(100))
    description = db.Column(db.String(200))
    location = db.Column(db.String(200))
    u_name = db.Column(db.String(100))
    password = db.Column(db.String(200), nullable = False)
    role_type = db.Column(db.Integer)
    created_on = db.Column(db.BigInteger)
    created_by = db.Column(db.Integer)
    image_url=db.Column(db.String(700))
    personnel_id=db.Column(db.String(200), unique=True)
    external_status=db.Column(db.String(200))


    def serialize(self):
        return {
            "user_id": self.user_id,
            "email":self.email,
            "login_id": self.login_id,
            "country": self.country,
            "department": self.department,
            "description": self.description,
            "location": self.location,
            "u_name": self.u_name,
            "role_type": self.role_type,
            "image_url":self.image_url,
            "created_on": self.created_on,
            "created_by": self.created_by,
            "personnel_id": self.personnel_id,
            "external_status":self.external_status,
            "password":self.password
        }
