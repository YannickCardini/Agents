import random
import re
import nltk
from nltk.corpus import wordnet

# TODO A continuer

mafia = wordnet.synsets("mafia")
afraid = wordnet.synsets("danger")
angry = wordnet.synsets("crazy")
peur = 1
colere = 0
mefiance = 2
bot_template = "BOT : {0}"
user_template = "USER : {0}"
peur_terms = "mafia|police|kill|threat|danger"
colere_terms = "paranoid|crazy"
rules = {'[H|h]i|ello': ["Hello.",
                         "Hi."],
         '[D|d]o you think (.*)': ['if {0}? Absolutely.', 'No chance'],
         '[D|d]o you remember (.*)': ['Did you think I would forget {0}',
                                      "Why haven't you been able to forget {0}", 'What about {0}', 'Yes .. and?'],
         'I want (.*)': ['What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"],
         'if (.*)': ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}', 'Really--if {0}'],
         'Are you (.*)': ["Do you think i'm {0}"],
         '[W|w]hy don\'t you (.*)': [" Do you believe I don't {0} ?",
                                     "Perhaps I will {0} in good time.",
                                     "Should you {0} yourself ?",
                                     "You want me to {0} ?"],
         '[B|b]ye': ["Goodbye. Thank you for talking to me."],
         '[S|s]orry': ["Please don't apologise.",
                       "Apologies are not necessary.",
                       "I've told you that apologies are not required."],
         'age|old': ["I'm 28 years old"],
         'family|spouse|married': ["I ride alone", "I live alone"],
         '[h|H]ow are you (.*)': ["OK", "I'm tired {0}"],
         '[w|W]ork': ["I work in the post office"],
         '[P|p]olice|cop[s]?': ["Cops don't do their job"],
         'name': ["I'm Frank Smith", "My name is Frank Smith"],
         '[W|w]hy are you (.*)': ["I souldn't be {0}", "Tt is independent of my own will."],
         '[W|w]ho (.*)': ["The police {0}"],
         'arrest': ["The law should arrest the bad people."],
         'bad': ["I try to stay clean."],
         'Mafa': ["I'm trying to stay out of their buissnes, but it's not easy"],
         '[A|a]re you sure': ["You don't believe me ?"]
         }


def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))
    print("##################################################")
    print("colere:", colere)
    print("mefiance:", mefiance)
    print("peur:", peur)
    print("##################################################")


def match_rule(rules, message):
    response, phrase = "In what whay ?", message

    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase


def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub("me", "you", message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub("my", "your", message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub("your", "my", message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub("you", "me", message)

    return message


def augmentePeur():
    global peur
    global mefiance
    peur += 2
    mefiance += 1
    if(mefiance >= 15):
        mefiance = 15
    if(peur >= 20):
        peur = 20


def augmenteColere():
    global colere
    global mefiance
    colere += 2
    mefiance += 1
    if(mefiance >= 15):
        mefiance = 15
    if(colere >= 20):
        colere = 20


def malveillance(noun):
    distanceDegree = 0.5
    syns = wordnet.synsets(noun)
    if(len(syns) == 0):
        return
    distance = mafia[0].wup_similarity(syns[0])
    if distance is None:
        return
    if distance > distanceDegree:
        augmentePeur()
    distance = afraid[0].wup_similarity(syns[0])
    if distance > distanceDegree:
        augmentePeur()
    distance = angry[0].wup_similarity(syns[0])
    if distance > distanceDegree:
        augmenteColere()


def bienveillance():
    global colere
    global peur
    global mefiance
    colere -= 1
    peur -= 0.5
    mefiance -= 0.4
    if(colere <= 0):
        colere = 0
    if(mefiance <= 0):
        mefiance = 0
    if(peur <= 0):
        peur = 0


def humeur(phrase, response):
    global mefiance
    tmp = mefiance
    def is_noun(pos): return pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(phrase + " " + response)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    for noun in nouns:
        malveillance(noun)
    if(mefiance == tmp):
        bienveillance()


def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    # Change état
    humeur(phrase, response)
    return response
#####################################################


# send_message("Hello sir, how are you feeling today ?")
# send_message("How old are you ?")
# send_message("What about you family ?")
# send_message("How old are you ?")
# send_message("What can of job are you working for ?")
# send_message("Do you remember why your in hospital ?")
# send_message("Are you in danger ?")
# send_message("Are you crazy ?")
# send_message("Are you in trouble with the police ?")
while True:
    said = input('> ')
    if(mefiance > 9):
        print('\033[92m', "I don't want to talk to you anymore, goodbye.", '\033[0m')
        break
    response = respond(said)
    print('\033[92m', response, '\033[0m')
    print("##################################################")
    print("colere:", colere)
    print("mefiance:", mefiance)
    print("peur:", peur)
    print("##################################################")
    if response.split(" ")[0] == "Goodbye.":
        break
