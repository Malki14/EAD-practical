class GrandParents:

    def __init__(self):
        pass

    def LandProperty(self):
        print("  Property inherit from Grand Parents ")


class Parents(GrandParents):

    def __init__(self):
        pass

    def HouseProperty(self):
        print("  Property inherit from  Parents ")


class Childs(Parents):

    def __init__(self):
        pass

    def VehicleProperty(self):
        print(" Vehicle buy from Child ")

    
    def LandProperty(self):
        print(" Land property convert to commecial building ")


akash = Childs()
akash.LandProperty()
akash.HouseProperty()
akash.VehicleProperty()
