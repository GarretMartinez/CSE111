from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners_original = ["the", "one"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1, 'present')
        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners_original

    plural_determiners_special = ["the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(2, 'present')
        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in plural_determiners_special

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2, 'future')

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single determiners.

    single_nouns = ['adult', 'bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'woman']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        noun = get_noun(1)
        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert noun in single_nouns

    # 2. Test the plural determiners.

    plural_nouns = ['adults', 'birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'women']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        noun = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert noun in plural_nouns

def test_get_verb():
    # 1. Test the single determiners.

    verbs_past = ['drank', 'ate', 'grew', 'laughed', 'thought', 'ran', 'slept', 'talked', 'walked', 'wrote']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        verb = get_verb(1, 'past')
        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert verb in verbs_past

    # 2. Test the plural determiners.

    single_verbs_present = ['drinks', 'eats', 'grows', 'laughs', 'thinks', 'runs', 'sleeps', 'talks', 'walks', 'writes']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        verb = get_verb(1, 'present')

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert verb in single_verbs_present

    plural_verbs_present = ['drink', 'eat', 'grow', 'laugh', 'think', 'run', 'sleep', 'talk', 'walk', 'write']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        verb = get_verb(2, 'present')

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert verb in plural_verbs_present

    future_verbs = ['will drink', 'will eat', 'will grow', 'will laugh', 'will think', 'will run', 'will sleep', 'will talk', 'will walk', 'will write']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        verb = get_verb(1, 'future')

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert verb in future_verbs

def test_get_preposition():
    prepo = ["about", "above", "across", "after", "along", 
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(4):
        preposition = get_preposition()
        assert preposition in prepo

def test_get_prepositional_phrase():
    for _ in range(4):
        prep_phrase = get_prepositional_phrase(1, 'past')
        assert prep_phrase in prep_phrase
        prep_phrase = get_prepositional_phrase(2, 'past')
        assert prep_phrase in prep_phrase
        prep_phrase = get_prepositional_phrase(1, 'present')
        assert prep_phrase in prep_phrase
        prep_phrase = get_prepositional_phrase(2, 'present')
        assert prep_phrase in prep_phrase
        prep_phrase = get_prepositional_phrase(1, 'future')
        assert prep_phrase in prep_phrase
        prep_phrase = get_prepositional_phrase(2, 'future')
        assert prep_phrase in prep_phrase


pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])