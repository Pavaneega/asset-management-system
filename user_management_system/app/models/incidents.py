from instance import db

class incidents(db.Model):
    #__table_args__ = {"schema":"form_builder"}
    __tablename__ = "incidents"

    incident_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    created_on = db.Column(db.BigInteger)
    created_by = db.Column(db.Integer)

    def serialize(self):
        return {
            "incident_id": self.incident_id,
            "created_on": self.created_on,
            "created_by": self.created_by
        }