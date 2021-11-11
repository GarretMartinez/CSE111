def main():
    pos_score = 0
    neg_score = 0
    print('This program is an implementation of the Rosenberg Self-Esteem Scale.\
    This program will show you ten statements that you could possibly\
    apply to yourself. Please rate how much you agree with each of the\
    statements by responding with one of these four letters:')

    print()
    print('D means you strongly disagree with the statement.') 
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')
    print()


    print('I feel that I am a person of worth, at least on an equal plane with others.')
    pos_score += positive_score(input('Enter D, d, a, or A: '))
    print('I feel that I have a number of good qualities.')
    pos_score += positive_score(input('Enter D, d, a, or A: '))
    print('All in all, I am inclined to feel that I am a failure.')
    neg_score += negative_score(input('Enter D, d, a, or A: '))
    print('I am able to do things as well as most other people.')
    pos_score += positive_score(input('Enter D, d, a, or A: '))
    print('I feel I do not have much to be proud of.')
    neg_score += negative_score(input('Enter D, d, a, or A: '))
    print('I take a positive attitude toward myself.')
    pos_score += positive_score(input('Enter D, d, a, or A: '))
    print('On the whole, I am satisfied with myself.')
    pos_score += positive_score(input('Enter D, d, a, or A: '))
    print('I wish I could have more respect for myself.')
    neg_score += negative_score(input('Enter D, d, a, or A: '))
    print('I certainly feel useless at times.')
    neg_score += negative_score(input('Enter D, d, a, or A: '))
    print('At times I think I am no good at all.')
    neg_score += negative_score(input('Enter D, d, a, or A: '))

    total_score = pos_score + neg_score
    print()
    print(f'You have a score of {total_score}')

def positive_score(score):
    if score == 'A':
        points = 3
    elif score == 'a':
        points = 2
    elif score == 'd':
        points = 1
    elif score == 'D':
        points = 0
    return points

def negative_score(score):
    if score == 'A':
        points = 0
    elif score == 'a':
        points = 1
    elif score == 'd':
        points = 2
    elif score == 'D':
        points = 3
    return points


main()