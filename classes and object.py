
class rentel_houses:
    def __init__(self,no,village,rent,colour,delour):
        self.no = no
        self.village = village
        self.rent = rent
        self.colour = colour 
        self.delour = delour
    def info(self):
        print(f"the house no is {self.no} and the village of house is {self.village} rant of house is {self.rent} and the colour is {self.colour}")
A1 = rentel_houses
A1.info()







