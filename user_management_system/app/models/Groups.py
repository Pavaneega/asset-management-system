from instance import db


class Groups(db.Model):
    #__table_args__ = {"schema":"app_authentication"}
    __tablename__ = "groups"

    group_id = db.Column(db.Integer, primary_key = True)
    group_name = db.Column(db.String(100),unique=True, nullable=False)
    created_by = db.Column(db.Integer, nullable=True)
    created_by_name = db.Column(db.String(150))
    created_at = db.Column(db.BigInteger, nullable=True)
    last_updated_at = db.Column(db.BigInteger, nullable=True)
    group_type=db.Column(db.String(150))
    function_id = db.Column(db.String(100))


    def serialize(self):
        return {
            "group_id": self.group_id,
            "group_name": self.group_name,
            "group_type":self.group_type,
            "created_by":self.created_by,
            "created_by_name":self.created_by_name,
            "created_at":self.created_at,
            "last_updated_at":self.last_updated_at,
            "function_id":self.function_id
        }


class Group_users(db.Model):
    __tablename__ = "Group_users"
    id = db.Column(db.Integer, primary_key = True)
    group_name = db.Column(db.String(100))
    user_id = db.Column(db.String(100), nullable=True)
    add_at = db.Column(db.BigInteger, nullable=True)
    add_by = db.Column(db.BigInteger, nullable=True)



    def serialize(self):
        return {
            "group_name": self.group_name,
            "user_id": self.user_id,
            "add_at":self.add_at,
            "add_by":self.add_by,

        }