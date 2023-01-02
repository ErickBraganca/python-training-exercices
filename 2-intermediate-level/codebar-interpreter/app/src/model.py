# Define a class of structured barcode functions.
class Barcode_Rules():
    #Return the region based in the range code
    def get_region(data):
        if data >= 1 and data <= 99:
            return "Sudeste" 
        elif data >= 100 and data <= 199:
            return "Sul"
        elif data >= 201 and data <= 299:
            return "Centro-Oeste"
        elif data >= 300 and data <= 399:
            return "Nordeste"
        else:
            return {'error': 101}

    #Return product type based in the code
    def get_product_type(data):
        if data == '001':
            return "Joias"
        elif data == '111':
            return "Livros"
        elif data == '333':
            return "Eletrônicos"
        elif data == '555':
            return "Bebidas"
        elif data == '888':
            return "Brinquedos"
        else:
            return {'error': 102}