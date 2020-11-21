import datefinder
import re
from random import randint
from geotext import GeoText

DESTINATION_CITY = None
DEPART_CITY = None
DEPART_TIME = None
RETURN_TIME = None
RESERVATION_NAME = None

def confirmationFlight():
    global DESTINATION_CITY
    global DEPART_CITY
    global DEPART_TIME
    global RETURN_TIME
    global RESERVATION_NAME
    sentence_end = " returning on " + str(RETURN_TIME) + " ?" if RETURN_TIME is not None else " ?"
    print("Do you want to go from "+ DEPART_CITY + " to " + DESTINATION_CITY + " on " + str(DEPART_TIME) + sentence_end)
    yesNo = input()
    yes = re.match('^[Y|y]es$',yesNo)
    no = re.match('^[N|n]o$',yesNo)
    if(no):
        DESTINATION_CITY = None
        DEPART_CITY = None
        DEPART_TIME = None
        RETURN_TIME = None
        RESERVATION_NAME = None
        main()
    elif(yes):
        print("I have confirmed the following flight: flight " + str(randint(100, 500)) + " on " + str(DEPART_TIME) + " from " + DEPART_CITY + " to " + DESTINATION_CITY )
        if(RETURN_TIME is not None):
            print("and the return flight on " + str(RETURN_TIME))
        print("Thanks you for booking with me. Goodbye.")
    else:
        confirmationFlight()


def retour():
    print("What date do you want to return ?")
    returnDate = input()
    matches = list(datefinder.find_dates(returnDate))
    if len(matches) > 0:
        global RETURN_TIME
        RETURN_TIME = matches[0]
        confirmationFlight()
    else:
        retour()

def isItOneWayTrip():
    print("Is it a one-way trip ?")
    yesNo = input()
    yes = re.match('^[Y|y]es$',yesNo)
    no = re.match('^[N|n]o$',yesNo)
    if(yes):
        confirmationFlight()
    elif(no):
        retour()
    else:
        isItOneWayTrip()

def extractData(input_string,depart=None):
    matches = list(datefinder.find_dates(input_string))
    if len(matches) > 0:
        global DEPART_TIME
        DEPART_TIME = matches[0]
    places = GeoText(input_string)
    global DESTINATION_CITY
    global DEPART_CITY
    if(len(places.cities) == 1):
        if(depart is None):
            DESTINATION_CITY = places.cities[0]
        else:
            DEPART_CITY = places.cities[0]
    elif(len(places.cities) > 1):
        DESTINATION_CITY = places.cities[0]
        DEPART_CITY = places.cities[1]

def main():
    global DESTINATION_CITY
    global DEPART_CITY
    global DEPART_TIME
    global RESERVATION_NAME

    if(DESTINATION_CITY is None):
        print("Where do you want to go ?")
        dest = input()
        extractData(dest)
        main()
    elif(DEPART_CITY is None):
        print("What city are you leaving from ?")
        dep = input()
        extractData(dep,depart=True)
        main()
    elif(DEPART_TIME is None):
        print("What's the departure date ?")
        departure_date = input()
        extractData(departure_date)
        main()
    else:
        isItOneWayTrip()


if __name__ == "__main__":
    print("Hello. My name is GUS. I can help you plan a simple trip by air. Where do you want to go ?")
    input_string = input()
    extractData(input_string)
    main()
