from datetime import datetime

def main():

    gender = input('Enter your gender (M/F): ')
    birthdate = input('Enter your birthdate in the following format (YYYY-MM-DD): ')
    weight = float(input('Enter your weight in US pounds: '))
    height = float(input('Enter your height in US inches: '))

    kilog = kg_from_lb(weight)
    centi = cm_from_in(height)
    bmi = body_mass_index(kilog, centi)
    age = compute_age(birthdate)
    bmr = basal_metabolic_rate(gender, weight, height, age)

    print()
    print(f'Gender: {gender.upper()}')
    print(f'Age (years): {age} ')
    print(f'Height (cm): {centi:.2f} ' )
    print(f'Weight (kg): {kilog:.2f}')
    print(f'Body mass index: {bmi:.2f}')
    print(f'Basal metabolic rate: {bmr:.2f}')


def compute_age(birth):

    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthday.year

    if birthday.month > today.month or (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years

def kg_from_lb(weight):
    kilog = weight * 0.45359237 
    return kilog

def cm_from_in(height):
    centi = height * 2.54
    return centi

def body_mass_index(weight, height):

    bmi = (10000 * weight) / height ** 2
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    if gender.lower() == 'm':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

main()