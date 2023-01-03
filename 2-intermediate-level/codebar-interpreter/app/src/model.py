# Define a class of structured barcode functions.
class barcode_rules():
    # Return the region based in the range code
    def get_region(region):
        if (1 >= region <= 99):
            return "Sudeste"
        elif (100 >= region <= 199):
            return "Sul"
        elif (201 >= region <= 299):
            return "Centro-Oeste"
        elif (300 >= region <= 399):
            return "Nordeste"
        elif (400 >= region <= 499):
            return "Nordeste"
        else:
            return {'error': 101}
    # -----------------------------------------#
    # Vendor Getter

    def get_vendor(vendor):
        vendor_store = {
            '001': 'Joias',
            '111': 'Livros',
            '333': 'Eletrônicos',
            '555': 'Bebidas',
            '888': 'Brinquedos',
            'ERR': 'Not Registered'
        }
        try:
            return vendor_store[vendor]
        except KeyError:
            return vendor_store['ERR']
    # -------------------------------------------#
    # Product Type Getter

    def get_product(product):
        product_store = {
            '001': 'Joias',
            '111': 'Livros',
            '333': 'Eletrônicos',
            '555': 'Bebidas',
            '888': 'Brinquedos',
            'ERR': 'Not Registered'
        }
        try:
            return product_store[product]
        except KeyError:
            return product_store['ERR']