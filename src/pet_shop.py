# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"] 

def add_or_remove_cash(pet_shop, cash_transaction):
    pet_shop["admin"]["total_cash"] = pet_shop["admin"]["total_cash"] + cash_transaction
    return pet_shop["admin"]["total_cash"]

    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, new_sales):
    pet_shop["admin"]["pets_sold"] = pet_shop["admin"]["pets_sold"] + new_sales
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_type):
    from collections import Counter
    breed_number = Counter(pet_shop["pets"]["breed"] == breed_type)
    return breed_number