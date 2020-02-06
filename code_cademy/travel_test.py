#!/usr/bin/python2.7

destination = [
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "Sao Paulo, Brazil",
    "Cairo, Egypt"
]

attractions = [[] for x in destination]

test_traveler = [
    'Erin Wilks', 
    'Shanghai, China',
    ['historical site', 'art']
]

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        break
    except ValueError:
        return("Destination does not exist")
    if 
print(add_attraction())
    

def get_destination_index(dest):
    destination_index = destination.index(dest)
    return(destination_index)
print(get_destination_index("Paris, France"))

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = traveler.index(traveler_destination)
    return(traveler_destination_index, traveler_destination)
print(get_traveler_location(test_traveler))
  
    
  
  