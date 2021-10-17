# WRITE YOUR FUNCTIONS HERE

#Function 1 - Input - def test_pet_shop_name(self)
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

#Function 2 - Input - def test_total_cash(self)
def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

#Function 3 - Input - test_add_or_remove_cash__add & test_add_or_remove_cash__remove
def add_or_remove_cash(cc_pet_shop,value):
    sum = get_total_cash(cc_pet_shop) + value
    cc_pet_shop["admin"]["total_cash"] =sum
    cash = get_total_cash(cc_pet_shop)
    return cash

#Function 4 - Input - def test_pets_sold(self)
def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

#Function 5 - Input - test_increase_pets_sold(self)
def increase_pets_sold(cc_pet_shop,value):
    sum = get_pets_sold(cc_pet_shop) + value
    cc_pet_shop["admin"]["pets_sold"] =sum
    sold = get_pets_sold(cc_pet_shop)
    return sold

#Function 6 - Input - def test_stock_count(self)
def get_stock_count (cc_pet_shop):
    stock = 0
    for pet in cc_pet_shop["pets"]:
        stock +=1
    return stock

#Function 7 - Input - def test_all_pets_by_breed__found
        # & def test_all_pets_by_breed__not_found
def get_pets_by_breed (cc_pet_shop,breed):
    breedlist = []
    for animal in cc_pet_shop["pets"]:
        if (animal["breed"]==breed):
            breedlist.append (animal["breed"])
    return breedlist

def find_pet_by_name (cc_pet_shop,name):
    for animal in cc_pet_shop["pets"]:
        if (animal["name"]==name):
            pet = {"name":animal["name"]}
            return pet

