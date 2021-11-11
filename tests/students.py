import csv

def main():

    id_index = 0
    name_index = 1

    id = input('Enter a student ID: ')
    dictionary = student_dict(id_index)

    if id not in dictionary:
        print('No such student')
    else:
        value = dictionary[id]
        name = value[name_index]
        print(name)


def student_dict(id_index):

    students_id = {}
    with open('students.csv', "rt") as students:
        reader = csv.reader(students)
        next(reader)
        for row in reader:
            key = row[id_index]
            students_id[key] = row
    return students_id

            

if __name__ == "__main__":
    main()