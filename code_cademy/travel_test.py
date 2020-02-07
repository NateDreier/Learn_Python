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

def get_destination_index(destinations):
    destination_index = destination.index(destinations)
    return(destination_index)

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = traveler.index(traveler_destination)
    return(traveler_destination_index, traveler_destination)

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index]
        attractions_for_destination.append(attraction)
    except ValueError:
        print("destination not in list")
    return(destination_index)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])

def find_attraction(destinations, interests):
    attractions_in_city = attractions[get_destination_index(destinations)]
    attractions_with_interest = []
    possible_attractions = []
    attraction_tags = []
    test = []
    for i in attractions_in_city:
        # test.append(i)
        possible_attractions.append(i)
        for i in possible_attractions:
        # test.append(i[1])
        attraction_tags.append(i[1])
    for i in attraction_tags:
        # test.append(i)
        test1 = attraction_tags.index(i)
        if i[0] == interests:
        test.append(possible_attractions[attraction_tags.index(i)])
    return(test)
print(find_attraction("Paris, France", "art"))
