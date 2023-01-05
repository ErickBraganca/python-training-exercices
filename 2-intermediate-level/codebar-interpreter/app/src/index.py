# Importing modules
import model
rule_model = model.barcode_model

# Input and output variables
inputed_codes = ['001345550001001', '246145550001001']
invalid_codes = []
pack_list = []

# Interpreter inicializator
def init_interpreter(raw_codes):
    print("#-----Start Interpreter-----#")

    # Code validation to check right code nature
    def code_validator(raw_codes):
        print('#-----Start Code Validator-----#')
        for raw_code in raw_codes:
            valid_enumeration = raw_code.isdecimal()
            valid_quantity = len(raw_code)

            if (valid_quantity == 15 and valid_enumeration):
                print('Code Validated')
                code_slicer(raw_code)
            else:
                invalid_codes.append(raw_code)
                print('Code Invalid')
    # ----------------------------------------#    
    # Code splitation in specific sentence
    def code_slicer(valid_code):
        print('#-----Start Code slicer-----#')
    
        # Dummy Code Splited
        splited_code = {
            "origem":       valid_code[0:3],
            "destino":      valid_code[3:6],
            "identificador":valid_code[6:9],
            "vendedor":     valid_code[9:12],
            "produto":      valid_code[12:16],
        }
        packge_composer(splited_code)

    # Call the nterpoint in interpreter inicializator
    code_validator(raw_codes)
    print("#-----End Interpreter-----#")

    return pack_list
# ----------------------------------------#

# Packge composer
def packge_composer(splited_code):
    print("#-----Start Pack Configurator-----#")

    # Dummy of package object
    pack_object = {
        'origem':       '',
        'destino':      '',
        'identificador':'',
        'vendedor':     '',
        'produto':      '',
    }

    pack_object['origem'] = rule_model.get_region(splited_code['origem'])
    pack_object['destino'] = rule_model.get_region(splited_code['destino'])
    pack_object['vendedor'] = rule_model.get_vendor(splited_code['vendedor'])
    pack_object['produto'] = rule_model.get_product(splited_code['produto'])
    pack_object['identificador'] = pack_object['identificador']

    pack_list.append(pack_object)
# ----------------------------------------#

print(init_interpreter(inputed_codes))
