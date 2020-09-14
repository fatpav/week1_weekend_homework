# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"] 

def add_or_remove_cash(pet_shop, cash_transaction):
    pet_shop["admin"]["total_cash"] += cash_transaction
    
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, new_sales):
    pet_shop["admin"]["pets_sold"] += new_sales

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])   

def get_pets_by_breed(pet_shop, breed_type):
    # function needs to return a list
    # I need to grab breed names from pet shop and find the matching breed type
    # they need to go into the list and return the list
    found_pets = []
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["breed"] == breed_type:
            found_pets.append(pet)
    return found_pets
# this is going to add the matching pet breeds to the new list

def find_pet_by_name(pet_shop, pet_name):
    found_name = None
    for pet_handle in pet_shop["pets"]:
        if pet_handle["name"] == pet_name:
            found_name = pet_handle
    return found_name

def remove_pet_by_name(pet_shop, pet_leaving):
    for pet_gone in pet_shop["pets"]:
        if pet_shop["pets"]["name"] == pet_leaving:
            pop(pet_gone["name"])
    
# This little guy requires the function to loop through the dictionary until it finds a name then rmove the entry.

