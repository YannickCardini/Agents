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

## Examlpes

### Booking a one way flight from Nice to Paris on the 26 of May
```
> Hello. My name is GUS. I can help you plan a simple trip by air. Where do you want to go ?
I want to go to Paris from Nice leaving 26 of May

> Is it a one-way trip ?
yes

> Do you want to go from Nice to Paris on 2020-05-26 00:00:00 ?
yes

> I have confirmed the following flight: flight 333 on 2020-05-26 >00:00:00 from Nice to Paris
> Thanks you for booking with me. Goodbye.
```

### Booking a round trip from London to Tokyo the 30 ocotober to 25 of November

```
> Hello. My name is GUS. I can help you plan a simple trip by air. Where do you want to go ?
to Tokyo 

> What city are you leaving from ?
London

> What's the departure date ?
30/10/2020

> Is it a one-way trip ?
no

> What date do you want to return ?
25/11/2020

> Do you want to go from London to Tokyo on 2020-10-30 00:00:00 returning on 2020-11-25 00:00:00 ?
yes

> I have confirmed the following flight: flight 154 on 2020-10-30 00:00:00 from London to Tokyo
and the return flight on 2020-11-25 00:00:00
> Thanks you for booking with me. Goodbye.
```

### Client hesitating
```
> Hello. My name is GUS. I can help you plan a simple trip by air. Where do you want to go ?
I don't know

> Where do you want to go ?
What do you suggest ?

> Where do you want to go ?
Maybe New York

> What city are you leaving from ?
Rome  

> What's the departure date ?
15/01/2020

> Is it a one-way trip ?
maybe

> Is it a one-way trip ?
yes i guess

> Is it a one-way trip ?
yes

> Do you want to go from Rome to York on 2020-01-15 00:00:00 ?
no

> Where do you want to go ?
Berlin

> What city are you leaving from ?
Rome

> What's the departure date ?
the 15 of Juanary

> Is it a one-way trip ?
no

> What date do you want to return ?
20 of Juanary

> Do you want to go from Rome to Berlin on 2020-11-15 00:00:00 returning on 2020-11-20 00:00:00 ?
no

> Where do you want to go ?
...
```