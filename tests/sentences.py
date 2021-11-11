import random

def main():

    determiner = int(input('How many people are there? '))
    tense = input('What tense? ')
    count = 6
    start_short = 1
    start_long = 1

    while start_short <= count:

        word = get_determiner(determiner, tense)
        noun = get_noun(determiner)
        verb = get_verb(determiner, tense)

        print(f'{word} {noun} {verb}')
        start_short += 1

    while start_long <= count:

        word = get_determiner(determiner, tense)
        noun = get_noun(determiner)
        verb = get_verb(determiner, tense)
        preposition_phrase = get_prepositional_phrase(determiner, tense)

        print(f'{word} {noun} {verb} {preposition_phrase}')
        start_long += 1

def get_determiner(grammatical_number, tense):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if grammatical_number == 1: 
        words = ["the", "one"]
    elif grammatical_number != 1 and tense.lower() == "present":
        words = ["the"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(grammatical_number):
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if grammatical_number == 1:
        nouns = ['adult', 'bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'woman']

    else:
        nouns = ['adults', 'birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'women']

    noun = random.choice(nouns)
    return noun

def get_verb(grammatical_number, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense.lower() == 'past':
        verbs = ['drank', 'ate', 'grew', 'laughed', 'thought', 'ran', 'slept', 'talked', 'walked', 'wrote']

    elif grammatical_number == 1 and tense.lower() == 'present':
        verbs = ['drinks', 'eats', 'grows', 'laughs', 'thinks', 'runs', 'sleeps', 'talks', 'walks', 'writes']

    elif grammatical_number != 1 and tense.lower() == 'present':
        verbs = ['drink', 'eat', 'grow', 'laugh', 'think', 'run', 'sleep', 'talk', 'walk', 'write']

    elif tense.lower() == 'future':
        verbs = ['will drink', 'will eat', 'will grow', 'will laugh', 'will think', 'will run', 'will sleep', 'will talk', 'will walk', 'will write']


    verb = random.choice(verbs)
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along", 
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(determiner, tense):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    noun = get_noun(determiner)
    determiner = get_determiner(determiner, tense)
    prepositional_phrase = (f'{preposition} {determiner} {noun}')
    
    return prepositional_phrase

#main()
