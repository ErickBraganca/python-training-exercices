class barcode_model():
    # Region Getter
    def get_region(region):
        print("#-----Start Region Getter-----#")
        region_store = {
            'Sudeste':      {'min': 1,   'max':  99},
            'Sul':          {'min': 100, 'max': 200},
            'Centro-Oeste': {'min': 200, 'max': 299},
            'Nordeste':     {'min': 300, 'max': 399},
            'Norte':        {'min': 400, 'max': 499},
        }
        checked_region = {}
        for index in region_store:
            instance = region_store[index]
            inf = instance['min']  # Inferior Limit
            sup = instance['max']  # Superior Limit

            if (int(region) in range(inf, sup)):
                checked_region['code'] = region
                checked_region['key'] = index
            # ---------------------------------------#
        if ((len(checked_region)) != 0):
            return checked_region
        else:
            checked_region['code'] = region
            checked_region['key'] = 'None'

            return checked_region
    # -----------------------------------------#
    # Vendor Getter
    def get_vendor(vendor):
        print("#-----Start Vendor Getter-----#")
        vendor_store = {
            '001': 'Lojas A',
            '102': 'Lojas B',
            '103': 'Lojas C',
            '104': 'Lojas D',
            '105': 'Lojas E',
            'ERR': 'Not Registered'
        }
        checked_vendor = {}
        try:
            checked_vendor['code'] = vendor
            checked_vendor['key'] = vendor_store[vendor]
            return checked_vendor

        except KeyError:
            checked_vendor['code'] = vendor
            checked_vendor['key'] = vendor_store['ERR']
            return checked_vendor
    # -------------------------------------------#
    # Product Type Getter
    def get_product(product):
        print("#-----Start Product Getter-----#")
        product_store = {
            '001': 'Joias',
            '111': 'Livros',
            '333': 'Eletrônicos',
            '555': 'Bebidas',
            '888': 'Brinquedos',
            'ERR': 'Not Registered'
        }
        checked_product = {}
        try:
            checked_product['code'] = product
            checked_product['key'] = product_store[product]
            return  checked_product

        except KeyError:
            checked_product['code'] = product
            checked_product['key'] = product_store['ERR']
            return  checked_product
    # -------------------------------------------#
# -------------------------------------------#