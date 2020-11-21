# GUS

A very basic air travel system:
- It asks the user the city of departure
- It asks for a destination city
- It asks for a date
- He asks if the trip is round trip or
no

## Dependencies

- datefinder
- geotext
```
pip install datefinder
pip install geotext
```

## How it's work

The chatbot will ask you different question about your desired flight, but you can give him all information in the first question and he will extract everything from your sentence.
The date and the city are extracted from the input string thanks to the datefinder and geotext package.