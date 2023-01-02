#Importing modules
import model

model_parser = model.Barcode_Rules
inputed_code = '012345678910123'

#Cheking if the inputed code is válid
def barcode_validator(raw_code):
    chart_lenght = len(raw_code)
    if chart_lenght != 15:
        print("Código Inválido")
    else:
        print('-----Code Validated-----')
        barcode_slicer(raw_code)

#Slicing the barcode in specific sequence.
def barcode_slicer(validated_code):
    print('-----Start Code Split-----')

    #Dummy code splited
    splited_code = {
        'Origem':       '',
        'Destino':      '',
        'Identificador':'',
        'Vendedor':     '',
        'Produto':      '',
    }

    #Defining split parameters
    i = 0 #Start Increment
    s = 3 #End Increment

    #Iterating by code
    for prop in splited_code:
        splited_code[prop]= validated_code[i:i + s]
        i+=3
    print(splited_code)
    print('-----End Code Split-----')

barcode_validator(inputed_code)