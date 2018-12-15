#%%
import requests

def home():
    
    url = "http://127.0.0.1:5000/home/" 
    
    response = requests.get(url).json()
    
    return response

home()
#%%

import requests

def add_contact(name,phone):
    
    url = "http://127.0.0.1:5000/add_contact/{}/{}".format(name,phone)
    
    response = requests.put(url).json()
    
    return response


add_contact("pepe", 109292)
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

def delete_phone(name):
    
    url = "http://127.0.0.1:5000/delete_contact/" + name 
    
    response = requests.delete(url).json()
    
    return response

delete_phone("david")

#%%

import requests

def update_phone(name, new_phone):
    
    url = "http://127.0.0.1:5000/update_phone/" + name + "/" + str(new_phone)
    
    response = requests.post(url).json()
    
    return response

update_phone("yotroz",55555)

#%%     
