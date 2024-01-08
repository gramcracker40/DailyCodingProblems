# This problem was asked by Jane Street.

# The United States uses the imperial system of weights and
# measures, which means that there are many different, seemingly 
# arbitrary units to measure distance. There are 12 inches in a foot,
# 3 feet in a yard, 22 yards in a chain, and so on.

# Create a data structure that can efficiently convert a certain quantity 
# of one unit to the correct amount of any other unit. You should also 
# allow for additional units to be added to the system.

class DistanceConverter:
    '''
    built to hold a distance of a specific unit. 
    you can convert the distance by simply changing the unit
    available units

    'feet', 'inches', 'yards', 'chain' 
    '''
    ratios = {
        "feetinches": 12,
        "feetyards": 1/3,
        "feetchain": 1/66,
        "inchesfeet": 1/12, 
        "inchesyards": 1/36,
        "incheschain": 1/792, 
        "yardsinches": 36, 
        "yardsfeet": 3,
        "yardschain": 1/22,
        "chaininches": 792, 
        "chainfeet": 66, 
        "chainyards": 22
    }

    units = {"feet", "inches", "yards", "chain"}

    def __init__(self, distance:float, unit="inches", accuracy:int=5):
        '''
        set the starting distance, unit, and accuracy for the MeasurementConverter
        '''
        self.distance = distance
        self.unit = unit
        self.accuracy = accuracy

    def change_accuracy(self, new_accuracy:int):
        self.accuracy = new_accuracy

    def convert(self, unit):
        '''
        converts the initialized unit to a different valid measurement.
        '''
        try:
            factor = DistanceConverter.ratios[f"{self.unit}{unit}"]
            old_distance = self.distance
            self.distance *= factor
            
            old_unit = self.unit
            self.unit = unit
            print(f"""Successfully converted from {old_unit} to {unit}\n{old_distance} {old_unit} --> {round(self.distance,self.accuracy)} {unit}""")

        except KeyError as err:
            print(f"Conversion failed, {err} is not a valid conversion")


    def compare(self):
        '''
        shows the stats for the initialized unit compared to
          all other units of measurement
        '''
        other_units = {x for x in DistanceConverter.units 
                       if x != self.unit}

        print(f"{round(self.distance,self.accuracy)} {self.unit}")
        for unit in other_units:
            factor = DistanceConverter.ratios[f"{self.unit}{unit}"]
            print(f"{round(self.distance * factor, self.accuracy)} {unit}")

if __name__ =="__main__":
    test = DistanceConverter(12, unit="chain", accuracy=7)
    
    test.convert("inches")
    
    print("\nComparing...")
    test.compare()

