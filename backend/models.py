#contains all the database models

from config import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), unique= False, nullable=False)
    last_name = db.Column(db.String(80), unique= False, nullable= True )
    email = db.Column(db.String(120), unique=True , nullable=False)
    telephone = db.Column(db.String(10), unique = False, nullable = False)

    #converts fields into the dictionary
    # and then into the JSON object
    # API communication is through the JSON
    # use camel case in JSON
    # use snake case in SQL
    def to_json(self):
        return{
            "id":self.id,
            "firstName" : self.first_name,
            "lastName" : self.last_name,
            "email" : self.email,
            "mobileNumber" : self.telephone,
        }

