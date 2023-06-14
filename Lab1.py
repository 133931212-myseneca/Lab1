import datetime

def calculate_age():
    current_year = datetime.datetime.now().year
    try:
        birth_year = int(input("Enter your birth year: "))
        age = current_year - birth_year
        if age < 0:
            print("Invalid birth year! Please enter a valid year.")
        else:
            print("Your age is:", age)
    except ValueError:
        print("Invalid input! Please enter a valid year.")

calculate_age()

def helloWorld():
	print(‘Hello World’)


helloWorld()
