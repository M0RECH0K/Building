class Building:

    def __init__(self):
        self.numberOfFloors = 3
        self.buildingType = str(3)

    def __eq__(self, other):
        return other.numberOfFloors == self.numberOfFloors and other.buildingType == self.buildingType


Building1 = Building()
Building1.numberOfFloors = 3
Building1.buildingType = "Office"

Building2 = Building()
Building2.numberOfFloors = 3
Building2.buildingType = "Office"
print(Building1 == Building2)
