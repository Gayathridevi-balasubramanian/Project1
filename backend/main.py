# contain main endpoints i.e., localhost:5000/create_contact + data to create record
# can be seperated into many files in bigger project

# CRUD 
# request (GET, POST, PUT, PATCH, DELETE) + JSON data
# and response  status:{404,400,etc.,} + JSON data

from flask import request, jsonify
from config import app , db
from models import Contact

#decorator that specifies the route and methods
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    #use ORM(flasksqlalchemy) that uses the all of the Contact that exists in db
    json_contacts = list(map(lambda x : x.to_json(), contacts))
    # contacts is the list of objects of the Contact Class
    return jsonify({"contacts":json_contacts})
    # used to convert data into the Json

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    mobile_number = request.json.get("mobileNumber")

    if not first_name or not last_name or not email or not mobile_number:
        return (
            jsonify({"message":"You must include a first_name, last_name, email and mobilenumber "}),
            400,  # status message of the response
        )
    
    # first,  create a database object
    # second, add to the db session
    # finally commit and catch the exception
    # use postman to test the functionality
    new_contact = Contact(first_name=first_name, last_name=last_name,email=email, telephone=mobile_number)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message":str(e)}),400
    
    return jsonify({"message":"The User Created!"}) , 201

@app.route("/update_contact/<int:user_id>",methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message":"The User does not exists!"}), 404 
    data = request.json
    contact.first_name = data.get("firstName",contact.first_name)
    contact.last_name = data.get("lastName",contact.last_name)
    contact.email = data.get("email",contact.email)
    contact.telephone = data.get("mobileNumber",contact.telephone)

    db.session.commit()
    return jsonify({"message":"The User Information is updated!"}), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message":"There is no such user!"}) , 404
    
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message":"The User is Deleted!"}) , 200



if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
        # create all the different models i.e.,contact that are imported here
        # does this when it is not already created
    
    app.run(debug=True)
    # tells that to run the app file if only running the main
    # not run the app on import but only on the main.py runtime