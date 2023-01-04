# Importing modules
import model

rule_model = model.barcode_rules
inputed_code = "001334555001001"

# Cheking if the inputed code is válid
def barcode_validator(raw_code):
    chart_lenght = len(raw_code)
    if chart_lenght != 15:
        print("Código Inválido")
    else:
        print("-----Code Validated-----")
        barcode_slicer(raw_code)
#----------------------------------------#

# Slicing the barcode in specific sequence.
def barcode_slicer(validated_code):
    print("-----Start Code Split-----")

    # Dummy code splited
    splited_code = {
        "origem": "",
        "destino": "",
        "identificador": "",
        "vendedor": "",
        "produto": "",
    }

    # Defining split parameters
    i = 0  # Start Increment
    s = 3  # End Increment

    # Iterating by code
    for prop in splited_code:
        splited_code[prop] = validated_code[i : i + s]
        i += 3
    #-------------------------------------#
    packge_composer(splited_code)
    print("-----End Code Split-----")
#----------------------------------------#

#Packge composer
def packge_composer(splited_code):
    print("-----Start Pack Configuration-----")
    pack_list = []
    pack_object = {**splited_code}

    pack_object['origem'] = rule_model.get_region(splited_code['origem'])
    pack_object['destino'] = rule_model.get_region(splited_code['destino'])
    pack_object['vendedor'] = rule_model.get_vendor(splited_code['vendedor'])
    pack_object['produto'] = rule_model.get_product(splited_code['produto'])
    pack_object['identificador'] = pack_object['identificador']

    pack_list.append(pack_object)
#----------------------------------------#
barcode_validator(inputed_code)



