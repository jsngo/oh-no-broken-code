# I can't be bothered to think of a Hallowe'en costume so
# can you help me generate one randomly?
import random

nouns = []
adjectives = []

with open('things.txt') as f:
    # We don't want those stinky \n newline characters
    # so we call strip() before adding it to our nouns list.
    for line in f:
        nouns.append(line.strip())

with open('descriptors.txt') as f:
    for line in f:
        adjectives.append(line.strip())


def generate_costume():
    # pick something random from the nouns and adjectives list
    noun = random.choice(nouns)
    adj = random.choice(adjectives)
    return (noun, adj)


while True:
    (noun, adjective) = generate_costume()
    print "You go dressed as a {} {} to the party.".format(adjective, noun)
    happy = raw_input("Are you happy with this choice? ")

    # Check if the user typed something like 'yes' or 'y' and
    # quit the program if they are happy.
    if happy == "yes" or happy == "y":
        exit()
    else:
        print "OK, I will choose another costume. Hold on..."
        print