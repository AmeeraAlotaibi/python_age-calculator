from datetime import date


def get_dob():
    # write code here
    year = int(input("enter your birth year "))
    month = int(input("enter your birth month "))
    day = int(input("enter your birth day "))
    dob = date(year, month, day)
    return dob


def get_age(dob):
    # write code here
    today = date.today()
    age = today - dob
    return age


def main():
    # write code here
    dob = get_dob()
    today = date.today()
    age = int((today - dob).days / 365)
    if dob < today:
        print(f"You are {age} years old!")
    else:
        print("You can't be born in the future!")


if __name__ == '__main__':
    main()
