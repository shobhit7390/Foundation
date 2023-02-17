# fstrings

# format()
letter="Hey my name is {} and I am from {}"

name="Shobhit"
country="India"

print(letter.format(name,country))

txt="For only {price:.2f} dollars"
print(txt.format(price=49.0999))


# f-strings
print(f"Hello, this is {name} from {country}")

price=49.899994
print(f"Only for {price:.2f} dollars")


# -------- docstrings ---------
# It is written just above the definition of function or just below the func name

def square(n):
    '''Takes in a number b and return the square of it'''
    print(n**3)

square(5)
print(square.__doc__)
