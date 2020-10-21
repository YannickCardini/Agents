import random
import re

rules = {
    '[H|h][i|ello]': ["How do you do.  Please state your problem.",
                      "Hi.  What seems to be your problem"],
    '[D|d]o you think (.*)': ['if {0}? Absolutely.', 'No chance'],
    '[D|d]o you remember (.*)': ['Did you think I would forget {0}', "Why haven't you been able to forget {0}", 'What about {0}', 'Yes .. and?'],
    '[I|i] want (.*)': ['What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"],
    '[I|i]f (.*)': ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}', 'Really--if {0}'],
    '[W|w]hy don\'t you (.*)': [" Do you believe I don't {0} ?",
                                "Perhaps I will {0} in good time.",
                                "Should you {0} yourself ?",
                                "You want me to {0} ?"],
    '[B|b]ye': ["Goodbye. Thank you for talking to me."],
    '[S|s]orry': ["Please don't apologise.",
                  "Apologies are not necessary.",
                  "I've told you that apologies are not required."]
}


def getDefault():
    return random.choice([
        " I'm not sure I understand you fully.",
        " Please go on.",
        " What does that suggest to you ?",
        " Do you feel strongly about discussing such things ?"
    ])


def match_rule(rules, message):
    response, phrase = getDefault(), None

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


def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response


# Send the messages
# send_message("do you remember your last birthday")
# send_message("do you think humans should be worried about AI")
# send_message("I want a robot friend")
# send_message("what if you could be anything you wanted")
print("Hello user, i'm Eliza")
while True:
    said = input('> ')
    response = respond(said)
    print(response)
    if response.split(" ")[0] == "Goodbye.":
        break
