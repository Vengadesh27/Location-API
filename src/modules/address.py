from geopy.geocoders import Nominatim

class Address():

    def __init__(self) -> None:
        self.geolocator = Nominatim(user_agent="geoapiExercises")
        self.lat = 0.00
        self.long = 0.00

    def location_address(self , lat , long):
        return  self.geolocator.reverse(lat+","+long)

    
