import re

def main():

    #questions used for files later
    Q1 = '1. When was it written?'
    Q2 = '2. Who was the author?'
    Q3 = '3. What is the context of the document?'
    Q4 = '4. Where can I go to see this online?'
    Q5 = '5. Exit'


    #print availible files and have user pick one
    print()
    print('Below are 3 different files')
    print()

    print('1: Family Proclamation')#churchofjesuschrist.org
    print('2: Gettysburg Address') #abrahamlincolnonline.org
    print('3: Wrecked - Imagine Dragons')#musixmatch.com

    print()
    filename = input('Enter the file number you would like to read: ')
    if filename == '1':
        filename = 'proclamation.txt'
    elif filename == '2':
        filename = 'gettysburg.txt'
    elif filename == '3':
        filename = 'wrecked.txt'

    #call function to read/print file
    print()
    data = open_file(filename)
    print(data)
    print()

    #ask user for a word to search, then call function to count occurences and total word count
    word = input('What word would you like to search for? ')
    index = find_word(data, word)
    print(f'The word "{word}" was found {index} times in the file')


    #ask user if they would like to know more about the file, if yes then call other function
    answer = input('Would you like to know more about the file? [Y/N]: ')
    if answer == 'Y' or answer == 'y' or answer == 'yes' or answer == 'Yes':
        if filename == 'proclamation.txt':
            proclamation(Q1,Q2,Q3,Q4,Q5)
        elif filename == 'gettysburg.txt':
            gettysburg(Q1,Q2,Q3,Q4,Q5)
        elif filename == 'wrecked.txt':
            wrecked(Q1,Q2,Q3,Q4,Q5)
    elif answer == "N" or answer == 'n' or answer == 'no' or answer == 'NO':
        print('Have a good day!')
        quit()


#function for reading file
def open_file(filename):

    with open(filename, encoding="utf8") as file:

        # use function that will read from the opened file.
        data = file.read()
        return data
        #https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
        #https://pythonexamples.org/python-read-text-file/
        #https://www.w3schools.com/python/python_file_open.asp


#function that will find the searched word and count how many words are in the file
def find_word(filename, word):
    index = 0
    words = 0

    seperate = filename.split()
    for item in seperate:
        words += 1

    #https://www.w3schools.com/python/ref_string_split.asp
    #https://appdividend.com/2021/05/12/how-to-split-string-with-multiple-delimiters-in-python/
    #https://pynative.com/python-regex-split/

    #use re module to take out punctuation that will sway searched word occurences
    tot_seperate = re.split(r'[.,;:()?!-"\s"]', filename)

    for item in tot_seperate:
        if item == word or item == word.capitalize() or item == word.upper() or item == word.lower():
            index += 1
            

    print(f'There are {words} words in the file')
    return index

#the following 3 functiona re just questions about each file
def proclamation(Q1,Q2,Q3,Q4,Q5):
    print()
    print('Here are some questions about the Family Proclamation to the World')
    print()
    print(Q1)
    print(Q2)
    print(Q3)
    print(Q4)
    print(Q5)
    print()
    q_num = input('Enter the number index of the question you want to see: ')
    print()
    while q_num == '1' or q_num == '2' or q_num == '3' or q_num == '4' or q_num == '5':
        if q_num == '1':
            print('The Family Proclamation was first read on September 23, 1995')
            print()
        elif q_num == '2':
            print("This document was written and produced by the first presidency and the members of the Quorum of the 12 apostles of The Church of Jesus Christ of Latter Day Saints")
            print()
        elif q_num == '3':
            print("This document was first read as part of President Gorden B. Hinckley's " +
                    "message at the general relief society meeting held in Salt Lake City Utah. " +
                    "The proclamation teaches about the importance of families and the role of " +
                    "families in God's plan. This proclamation is the 6th one produced by the church, " +
                    "while other teachings are directed specifically at members of the church, " +
                    "proclamations are meant for the world.")
            print()
        elif q_num == '4':
            print('You can view the proclamation and other information on www.churchofjesuschrist.org')
            print()
        elif q_num == '5':
            end = input('Type "E" to end the program, type "R" to read another file: ')
            if end == "E" or end == "e":
                print()
                print('Have a good day!')
                quit()
            elif end == "R" or end == "r":
                main()

        q_num = input('Enter the number index of the question you want to see: ')
        print()


def gettysburg(Q1,Q2,Q3,Q4,Q5):
    print()
    print('Here are some questions about the Gettysburg Address')
    print()
    print(Q1)
    print(Q2)
    print(Q3)
    print(Q4)
    print(Q5)
    print()
    q_num = input('Enter the number index of the question you want to see: ')
    print()
    while q_num == '1' or q_num == '2' or q_num == '3' or q_num == '4' or q_num == '5':
        if q_num == '1':
            print('The Gettysburg Address was given in speech on November 19, 1863')
            print()
        elif q_num == '2':
            print("The speech was written and delivered by the 16th President of the U.S. Abraham Lincoln")
            print()
        elif q_num == '3':
            print("Abraham Lincoln gave his address at the dedication of the Solldier's National Cemetery " +
                    "in Gettysburg Pennsylvania. It had been 4 and a half months after the Union armies " +
                    "defeated the Confederacy at the Battle of Gettysburg during the American Civil War. " +
                    "There are 5 known manuscripts of the address currently known, the Bliss version " +
                    "is considered by many as the standard text.")
            print()
        elif q_num == '4':
            print('You can see all of the addresses and history on Wikipedia or www.abrahamlincolnonline.org')
            print()
        elif q_num == '5':
            end = input('Type "E" to end the program, type "R" to read another file: ')
            if end == "E" or end == "e":
                print()
                print('Have a good day!')
                quit()
            elif end == "R" or end == "r":
                main()

        q_num = input('Enter the number index of the question you want to see: ')
        print()

def wrecked(Q1,Q2,Q3,Q4,Q5):
    print()
    print('Here are some questions about Wrecked by Imagine Dragons')
    print()
    print(Q1)
    print(Q2)
    print(Q3)
    print(Q4)
    print(Q5)
    print()
    q_num = input('Enter the number index of the question you want to see: ')
    print()
    while q_num == '1' or q_num == '2' or q_num == '3' or q_num == '4' or q_num == '5':
        if q_num == '1':
            print('The song itself was released July 2nd, 2021')
            print()
        elif q_num == '2':
            print("Wrecked was written and published by famous pop rock band Imagine Dragons, sung by Dan Reynolds")
            print()
        elif q_num == '3':
            print("Wrecked is the 3rd single on their 5th studio album Mercury - Act 1. " +
                    "Although the single was released in July, the full album was made availible in September of 2021. " +
                    "The song was inspired by Dan Reynolds' sister-in-law, Alisha Durtschi Reynolds, " +
                    "who passed away from cancer. Dan expressed that music had always been his refuge " +
                    "and that the song was a way of dealing with it all. The song had reached number 11 on " +
                    "billboard top 100 and number 4 on rock airplay billboard.")
            print()
        elif q_num == '4':
            print('You can see more charts and background about Wrecked or Imagine Dragons on Wikipedia or listen to the song on any popular music app')
            print()
        elif q_num == '5':
            end = input('Type "E" to end the program, type "R" to read another file: ')
            if end == "E" or end == "e":
                print()
                print('Have a good day!')
                quit()
            elif end == "R" or end == "r":
                main()

        q_num = input('Enter the number index of the question you want to see: ')
        print()
        

if __name__ == "__main__":
    main()