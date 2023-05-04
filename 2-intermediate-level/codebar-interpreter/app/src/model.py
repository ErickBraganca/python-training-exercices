class Package:
    # Constructor Method
    def __init__(self, origin, destination, company, vendor, product):
        # Computed Parameters
        self.origin = self.set_region(origin)
        self.destination = self.set_region(destination)
        self.company = self.set_company(company)
        self.vendor = self.set_vendor(vendor)
        self.product = self.set_product(product)
    # ----------------------------------------#
    # Region Getter
    def set_region(self, origin_code):
        region_store = {
            "Sudeste":      {"min": 1, "max": 99},
            "Sul":          {"min": 100, "max": 200},
            "Centro-Oeste": {"min": 200, "max": 299},
            "Nordeste":     {"min": 300, "max": 399},
            "Norte":        {"min": 400, "max": 499},
        }
        checked_region = {}
        for index in region_store:
            instance = region_store[index]
            inf = instance["min"]  # Inferior Limit
            sup = instance["max"]  # Superior Limit

            if int(origin_code) in range(inf, sup):
                checked_region["code"] = origin_code
                checked_region["key"] = index
            # ---------------------------------------#
        if (len(checked_region)) != 0:
            return checked_region
        else:
            checked_region["code"] = origin_code
            checked_region["key"] = "None"

            return checked_region
    # -----------------------------------------#
    # Vendor Getter
    def set_vendor(self, vendor_code):
        vendor_store = {
            "123": "Lojas A",
            "584": "Lojas B",
            "124": "Lojas C",
            "874": "Lojas D",
            "654": "Lojas E",
            "367": "Lojas F",
            "ERR": "Not Registered",
        }
        checked_vendor = {}
        try:
            checked_vendor["code"] = vendor_code
            checked_vendor["key"] = vendor_store[vendor_code]
            return checked_vendor

        except KeyError:
            checked_vendor["code"] = vendor_code
            checked_vendor["key"] = vendor_store["ERR"]
            return checked_vendor
    # -------------------------------------------#
    # Product Getter
    def set_product(self, product_code):
        product_store = {
            "001": "Joias",
            "111": "Livros",
            "333": "Eletrônicos",
            "555": "Bebidas",
            "888": "Brinquedos",
            "ERR": "Not Registered",
        }
        checked_product = {}
        try:
            checked_product["code"] = product_code
            checked_product["key"] = product_store[product_code]
            return checked_product

        except KeyError:
            checked_product["code"] = product_code
            checked_product["key"] = product_store["ERR"]
            return checked_product
    # -------------------------------------------#
    # Company Code Setter
    def set_company(self, company_code):
        return {"code": company_code, "key": "Company Code"}
    # -------------------------------------------#
    # Package Getter
    def get_package(self):
        package = {
            "origin": self.origin,
            "destination": self.destination,
            "vendor": self.vendor,
            "product": self.product,
            "company": self.company,
        }
        return package
