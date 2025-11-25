# name
# dob
# gender
# blood group
# occupation
# marital status
# phone
# next of kin
# insurance - true/false

# calculate age based on dob

# 1. create reg form dt captures following deatils
# 2. print details using f-string
# 3. if has insurance, give options of choosing btw 3 insurance plans (NHIS, OHIS, HMO)
# 4. capture the insurance details and print it out with the plan selected using f string

from datetime import date


print("Welcome to Age calc, please enter the following details as requested\n")

name = str(input("Enter your name: "))
dob_y = int(input("Enter your birth year: "))

print(
    """
    1. Jan
    2. Feb
    3. Mar
    4. Apr
    5. May
    6. Jun
    7. Jul
    8. Aug
    9. Sep
    10. Oct
    11. Nov
    12. Dec
    """
)
dob_m = int(input("Enter your birth month: "))

dob_d = int(input("Enter your birth day (1-31): "))

# calculate age based on date of birth
dob = date(dob_y, dob_m, dob_d)
age = date.today().year - dob.year
print(
    """
    Gender options
    1. Male
    2. Female
    3. Not specified
    """
)
genderOpt = int(input("Select your gender: "))
gender = "Not specified"
if (genderOpt==1):
    gender = "Male"
elif (genderOpt == 2):
    gender = "Female"


bloodGrp = str(input("Enter your blood group: "))

print(
    """
    Marital status
    1. Single
    2. Married
    3. Divorced
    """
)
maritalStatusOpt = int(input("Select your marital status: "))
maritalStatus = "Single"
if (maritalStatusOpt==2):
    maritalStatus = "Married"
elif (maritalStatusOpt == 3):
    maritalStatus = "Divorced"


# phone = str(input("Enter your phone: "))
# nextOfKin = str(input("Enter your next of kin : "))


hasInsurance = str(input("Do you have insurance (yes/no): "))
insurance = "No Insurance"
if (hasInsurance.lower() == "yes"):
    print(
    """
        Insurance plans
        1. NHIS
        2. OHIS
        3. HMO
        """
    )
    insurancePlan = int(input("Select your insurance paln: "))
    if (insurancePlan == 1):
        insurance = "NHIS"
    elif (insurancePlan == 2):
        insurance = "OHIS"
    elif (insurancePlan == 3):
        insurance = "HMO"
else:
    hasInsurance = "no"

formattedRes = f"Name: {name}\nAge: {age}\nGender: {gender}\nBlood Group: {bloodGrp}\nMarital Status: {maritalStatus}\nInsurance: {insurance}"
print(formattedRes)