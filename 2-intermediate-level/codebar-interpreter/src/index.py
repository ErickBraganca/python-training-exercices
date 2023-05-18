# Importing Package Module
from model import Package
from store import Controler

# Input and output variables
invalid_codes = []
package_list = []

code_list = [
    '034311555874001'
]   

# Interpreter Module
class Interpreter:
    # Interpreter inicializator.
    def init(self, code_list):
        print("#-----Start Interpreter-----#")
        for code in code_list:
            self.code_validator(code)
        print("#-----End Interpreter-----#")

        Controler.set_data('Packages', package_list)
        return package_list
    # ----------------------------------------#
    # Code validation to check right code nature
    def code_validator(self, raw_code):
        valid_enumeration = raw_code.isdecimal()
        valid_quantity = len(raw_code)

        if valid_quantity == 15 and valid_enumeration:
            print("Code Validated")
            self.package_composer(raw_code)
        else:
            invalid_codes.append(raw_code)
            print("Code Invalid")
    # ----------------------------------------#
    # Code splitation and package composer
    def package_composer(self, valid_code):
        # Code splitation
        origin_code =       valid_code[0:3]
        destination_code =  valid_code[3:6]
        company_code =      valid_code[6:9]
        vendor_code =       valid_code[9:12]
        product_code =      valid_code[12:16]
        # Dummy of package object

        package_instance = Package(
            origin_code, destination_code, company_code, vendor_code, product_code
        )
        package_object = package_instance.get_package()
        package_list.append(package_object)
    # ----------------------------------------#
# ----------------------------------------#
Interpreter().init(code_list)