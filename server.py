#%%

#Create an HTTP server and HTTP client to manage a
#phonebook. There should exist the following operations in the 
#phonebook:
#• add a contact (phone + name)
#• get a phone by name
#• delete a phone by name
#• update a phone by name
#Make sure you use JSON to communicate between client and server.

from flask import Flask, jsonify

server = Flask("phonebook")
        
phonebook = [{"name":"javi", "phone": 123},
             {"name":"yotroz", "phone": 456},
             {"name":"david", "phone": 789}]

@server.route("/home/")
def home():   
    return jsonify(phonebook)

@server.route("/add_contact/<name>/<phone>", methods=["PUT"])
def add_contact(name,phone):   
    new_contact = {"name":name, "phone":phone}
    phonebook.append(new_contact)
            
    return jsonify(str(new_contact) + " has been added to the phonebook")

@server.route("/get_phone/<name>")
def get_phone(name):   
    for contact in phonebook:
        if contact["name"] == name:
            number = contact["phone"]
    return jsonify(number)

@server.route("/delete_contact/<name>", methods=["DELETE"])
def delete_contact(name):
    index = next(index for index, dictionary in enumerate(phonebook) if dictionary['name'] == name)
    del phonebook[index]
    return jsonify(name + " has been deleted.")

@server.route("/update_phone/<name>/<new_phone>", methods=["POST"])
def update_phone(name, new_phone):

    for contact in phonebook:
        if contact["name"] == name:
            contact["phone"] = new_phone

    return jsonify("The phone number of " + name + " is now: " + str(new_phone))
    
server.run()
