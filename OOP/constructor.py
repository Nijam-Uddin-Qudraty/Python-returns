class Phone:
    def __init__(self,owner,brand,price):
        # add default values to class
        self.owner = owner
        self.brand = brand
        self.price = price
nub = Phone("abul","Nokia",99) # have to pass class valu while creating
print(nub.owner,nub.brand,nub.price)