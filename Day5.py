import re

# Define input file name
file_name = "day5data.txt"
# Define seed values to be mapped to locations
seeds = [1514493331, 295250933, 3793791524, 105394212, 828589016, 654882197, 658370118, 49359719, 4055197159, 59237418, 314462259, 268880047, 2249227634, 74967914, 2370414906, 38444198, 3291001718, 85800943, 2102534948, 5923540]

# Create map class that reads the relevant data from input file and performs the mapping described there
class Mapping:
    def __init__(self, mapping_name):
        self.mapping_name = mapping_name
        self.map_vals = []

    def get_mapping_data(self):
        with open(file_name,"r") as file:
            # Find file location of correct mappings and skip mapping heading line
            file.seek(file.read().find(self.mapping_name))
            next(file)
            for line in file:
                # Stop processing if you reach an empty line
                if not line.strip():
                    break
                self.map_vals.append([int(s) for s in re.findall(r'\b\d+\b', line)])

    def perform_map(self, input):
        for interval in self.map_vals:
            if interval[1] <= input <= interval[1] + interval[2] - 1:
                return interval[0] + (input - interval[1])
        return input

# Create maps for each section of input file
seed_soil_map = Mapping("seed-to-soil")
soil_fert_map = Mapping("soil-to-fertilizer")
fert_water_map = Mapping("fertilizer-to-water")
water_light_map = Mapping("water-to-light")
light_temp_map = Mapping("light-to-temperature")
temp_hum_map = Mapping("temperature-to-humidity")
hum_loc_map = Mapping("humidity-to-location")

# initialise maps with map data from file
seed_soil_map.get_mapping_data()
soil_fert_map.get_mapping_data()
fert_water_map.get_mapping_data()
water_light_map.get_mapping_data()
light_temp_map.get_mapping_data()
temp_hum_map.get_mapping_data()
hum_loc_map.get_mapping_data()

locations = map(hum_loc_map.perform_map, 
                list(map(temp_hum_map.perform_map, 
                        list(map(light_temp_map.perform_map, 
                                list(map(water_light_map.perform_map, 
                                        list(map(fert_water_map.perform_map, 
                                                list(map(soil_fert_map.perform_map, 
                                                        list(map(seed_soil_map.perform_map, seeds))
                                                        )))))))))))

# Find the smallest location value (part 1 answer = 579439039)
print(min(locations))

