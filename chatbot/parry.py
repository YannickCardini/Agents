import random
import re
import nltk
from nltk.corpus import wordnet

#TODO A continuer

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
rules = {'[D|d]o you think (.*)': ['if {0}? Absolutely.', 'No chance'],
         '[D|d]o you remember (.*)': ['Did you think I would forget {0}',
                                  "Why haven't you been able to forget {0}", 'What about {0}', 'Yes .. and?'],
         'I want (.*)': ['What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"],
         'if (.*)': ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}', 'Really--if {0}'],
         'Are you (.*)': ["Do you think i'm {0}"],
         '[h|H]ow are you (.*)': ["OK", "I'm tired"],
         '[w|W]ork' : ["I work in the post office"],
         '[P|p]olice|cop[s]?' : ["Cops don't do their job"]
         }


def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))
    print("colere:", colere)
    print("mefiance:", mefiance)
    print("peur:", peur)


def match_rule(rules, message):
    response, phrase = "default", None

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
    syns = wordnet.synsets(noun)
    distance = mafia[0].wup_similarity(syns[0])
    if distance > 0.3:
        augmentePeur()
    distance = afraid[0].wup_similarity(syns[0])
    if distance > 0.3:
        augmentePeur()
    distance = angry[0].wup_similarity(syns[0])
    if distance > 0.3:
        augmenteColere()

def bienveillance():
    global colere
    global peur
    global mefiance
    colere -= 1
    peur -= 0.5
    mefiance -= 0.2
    if(colere <= 0):
        colere = 0
    if(mefiance <= 0):
        mefiance = 0
    if(peur <= 0):
        peur = 0

#TODO ne pas faire bienviellance si malviellance augmente
def humeur(phrase, response):
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(phrase + " " + response)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    for noun in nouns:
        malveillance(noun)
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
    if(phrase is not None and response is not None):
        humeur(phrase, response)
    return response
#####################################################

send_message("Hello sir, how are you feeling today ?")
send_message("What can of job are you working for ?")
send_message("Do you remember why your in hospital ?")
send_message("Are you in danger ?")
send_message("Are you crazy ?")
send_message("Are you in trouble with the police ?")
