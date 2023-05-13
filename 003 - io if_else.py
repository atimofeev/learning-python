to_unit = 24
unit = "hours"


def days_to_units(days):
    if days > 0:
        return f"{days} days are {days * to_unit} {unit} {message}"
    else:
        return "Negative value entered"
        


user_input = input(f"Enter number of days for conversion into {unit}:\n")

user_input = int(user_input) # string to integer

print(days_to_units(user_input))