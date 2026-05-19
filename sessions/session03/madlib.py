import random

def get_word(prompt):
    return input(prompt)

def build_story(noun, verb, adjective, person, place):
    templates = [
        # Template 1: Celebrity Scandal 🌟
        f"BREAKING NEWS! {person.upper()} was caught {verb}ing with a {adjective} {noun} at {place.upper()}! "
        f"Witnesses say, 'It screamed *{verb.upper()} MORE!* and flew away.' "
        "The FBI is now involved. #ScandalOfTheYear",

        # Template 2: Alien Invasion 👽
        f"Alert! A {adjective} {noun} invaded {place} and kidnapped {person}! "
        f"To everyone's surprise, {person} taught the aliens to {verb}. "
        "Now they run a intergalactic bakery. Delicious.",

        # Template 3: Royal Romance 👑
        f"Once upon a time, Prince {person} fell in love with a {adjective} {noun} from {place}. "
        f"They vowed to {verb} together forever. The kingdom rejoiced... until the {noun} ate the royal throne. Oops.",

        # Template 4: Sports Drama 🏈
        f"At the {place} Olympics, {person.capitalize()} won gold by {verb}ing a {adjective} {noun}! "
        f"Critics called it 'the weirdest sport ever,' but the crowd chanted, '{verb.upper()}! {verb.upper()}!' "
        f"The trophy? A giant {noun}. History was made.",

        # Template 5: Make Your own 
        # GET CREATIVE!
    ]
    return random.choice(templates)

def main():
    print("\n🌟📚 THE ULTIMATE SILLY STORY GENERATOR 2.0 📚🌟\n")
    nn = get_word("Give me a noun: ")
    vb = get_word("Give me a verb: ")
    adj = get_word("Give me a adjective: ")
    per = get_word("Give me a person: ")
    pl = get_word("Give me a place: ")
  
    # Print out the Story
    story = build_story(nn, vb, adj, per, pl)
  
    print("\n🔥📖 HERE IS YOUR STORY 📖🔥")
    print("=" * 45)
    print(story)
    print("=" * 45)

if __name__ == "__main__":
    main()
