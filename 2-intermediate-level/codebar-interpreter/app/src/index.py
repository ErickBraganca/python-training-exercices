# Importing Package Module
from model import Package
import json
import os

# Input and output variables
invalid_codes = []
pack_list = []


# Interpreter inicializator
def init_interpreter(code_list):
    print("#-----Start Interpreter-----#")

    # Code validation to check right code nature
    def code_validator(code_list):
        for raw_code in code_list:
            valid_enumeration = raw_code.isdecimal()
            valid_quantity = len(raw_code)

            if valid_quantity == 15 and valid_enumeration:
                print("Code Validated")
                package_composer(raw_code)
            else:
                invalid_codes.append(raw_code)
                print("Code Invalid")

    # ----------------------------------------#
    # Code splitation and package composer
    def package_composer(valid_code):
        # Code splitation
        origin_code = valid_code[0:3]
        destination_code = valid_code[3:6]
        company_code = valid_code[6:9]
        vendor_code = valid_code[9:12]
        product_code = valid_code[12:16]
        # Dummy of package object
        package_instance = Package(
            origin_code, destination_code, company_code, vendor_code, product_code
        )
        package_object = package_instance.get_package()

        write_data(package_object)
        # pack_list.append(package_object)

    # ----------------------------------------#
    # Call the enterpoint in interpreter inicializator
    code_validator(code_list)
    print("#-----End Interpreter-----#")

    return pack_list


# ----------------------------------------#
def write_data(package):
    FILE_FOLDER = "data"
    FILE_NAME = "db.txt"
    JSON_SEPARATOR = (',', ':')

    FILE_PATH = os.path.join(FILE_FOLDER, FILE_NAME)
    print(FILE_PATH)

    with open(FILE_PATH, "a", encoding="utf-8") as content:
        json.dump(package, content, indent=4, separators=JSON_SEPARATOR)


init_interpreter(['288355555123888'])