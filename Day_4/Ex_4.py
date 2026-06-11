def age_validate(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    return age

try:
    age_validate(-1)

except ValueError as e:
    print("ValueError: ", e)