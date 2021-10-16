# WRITE YOUR FUNCTIONS HERE

#Function 1 - def test_pet_shop_name(self)
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

#Function 2 - def test_total_cash(self)
def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

#Function 3 - test_add_or_remove_cash__add & test_add_or_remove_cash__remove
def add_or_remove_cash(cc_pet_shop,value):
    sum = get_total_cash(cc_pet_shop) + value
    cc_pet_shop["admin"]["total_cash"] =sum
    cash = get_total_cash(cc_pet_shop)
    return cash


