__author__ = 'Craig'

def age_program():
    user_age = input("Please enter your age in years")
    age_seconds = int(user_age) * 365 * 24 * 60
    print("Your age in seconds " + str(age_seconds))



age_program()

