#%%

import requests

def add_contact(name,phone):
    
    url = "http://127.0.0.1:5000/add_contact/" + name + "/" + phone
    
    response = requests.get(url)
    new_contact = response.json()
    
    
    return new_contact , " Added to phonebook."

add_contact("leila","11122")

#%%
import requests

def get_phone(name):
    
    url = "http://127.0.0.1:5000/get_phone/" + name
    
    response = requests.get(url)
    number = response.json()       
             
    return "The phone number of " + name + " is " + str(number)

get_phone("javi")

#%%
import requests

def update_phone(name, new_phone):
    
    url = "http://127.0.0.1:5000/update_phone/" + name + "/" + new_phone
    
    response = requests.get(url)
    new = response.json()
    
    return "New phone of " + name + ": "  +  new

update_phone("yotroz",55555)

#%%
import requests

def delete_phone(name):
    
    url = "http://127.0.0.1:5000/delete_phone/" + name 
    
    response = requests.get(url)
    x = response.json()
    
    return x

delete_phone("david")

#%%
import requests

def home():
    
    url = "http://127.0.0.1:5000/home/" 
    
    response = requests.get(url)
    phonebook = response.json()
    
    return phonebook

home()

#%%

    