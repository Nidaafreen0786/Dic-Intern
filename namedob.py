import re
from datetime import datetime

class Validation:
    @staticmethod
    def rule_name(name):
        if not name:
            return False, "Name cannot be empty."
        if not re.match("^[A-Za-z\s'-]+$", name):
            return False, "Name contains invalid characters."
        if len(name) > 50:
            return False, "Name must be less than or equal to 50 characters."
        return True, "Valid name."

    @staticmethod
    def rule_mobile(mobile):
        if not mobile:
            return False, "Mobile number cannot be empty."
        if not mobile.isdigit():
            return False, "Mobile number must contain only digits."
        if len(mobile) != 10:
            return False, "Mobile number must be exactly 10 digits."
        return True, "Valid mobile number."

    @staticmethod
    def rule_email(email):
        if not email:
            return False, "Email cannot be empty."
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            return False, "Invalid email format."
        return True, "Valid email."

    @staticmethod
    def rule_dob(dob):
        if not dob:
            return False, "Date of birth cannot be empty."
        try:
            datetime.strptime(dob, "%d-%m-%Y")
        except ValueError:
            return False, "Date of birth must be in the format DD-MM-YYYY."
        return True, "Valid date of birth."

    @staticmethod
    def rule_aadhaar(aadhaar):
        if not aadhaar:
            return False, "Aadhaar number cannot be empty."
        if not aadhaar.isdigit():
            return False, "Aadhaar number must contain only digits."
        if len(aadhaar) != 12:
            return False, "Aadhaar number must be exactly 12 digits."
        return True, "Valid Aadhaar number."

    @staticmethod
    def rule_pan(pan):
        if not pan:
            return False, "PAN cannot be empty."
        pan_regex = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
        if not re.match(pan_regex, pan):
            return False, "Invalid PAN format."
        return True, "Valid PAN."

# Function to get runtime input and validate
def get_runtime_input_and_validate():
    validation = Validation()

    name = input("Enter your name: ")
    name_valid, name_msg = validation.rule_name(name)
    print(name_msg)

    mobile_valid = False
    while not mobile_valid:
        mobile = input("Enter your mobile number: ")
        mobile_valid, mobile_msg = validation.rule_mobile(mobile)
        print(mobile_msg)
        if not mobile_valid:
            print("Please re-enter a valid mobile number.")

    email = input("Enter your email: ")
    email_valid, email_msg = validation.rule_email(email)
    print(email_msg)

    dob = input("Enter your date of birth (DD-MM-YYYY): ")
    dob_valid, dob_msg = validation.rule_dob(dob)
    print(dob_msg)

    aadhaar_valid = False
    while not aadhaar_valid:
        aadhaar = input("Enter your Aadhaar number: ")
        aadhaar_valid, aadhaar_msg = validation.rule_aadhaar(aadhaar)
        print(aadhaar_msg)
        if not aadhaar_valid:
            print("Please re-enter a valid Aadhaar number.")

    pan_valid = False
    while not pan_valid:
        pan = input("Enter your PAN: ")
        pan_valid, pan_msg = validation.rule_pan(pan)
        print(pan_msg)
        if not pan_valid:
            print("Please re-enter a valid PAN number.")

if __name__== "__main__":
    get_runtime_input_and_validate()