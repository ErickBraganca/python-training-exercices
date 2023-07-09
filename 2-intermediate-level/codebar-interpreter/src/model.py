from store import Controler

class Package:
    # Constructor Method
    def __init__(self, origin, destination, company, vendor, product):
        # Computed Parameters
        self.origin =       self.set_region(origin)
        self.destination =  self.set_region(destination)
        self.company =      self.set_company(company)
        self.vendor =       self.set_vendor(vendor)
        self.product =      self.set_product(product)
    # ----------------------------------------#
    # Region Setter
    def set_region(self, origin_code):
        regions_store = Controler.get_data("Regions")
        checked_region = {}
        for index in regions_store:
            instance = regions_store[index]
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
    # Vendor Setter
    def set_vendor(self, vendor_code):
        vendors_store = Controler.get_data("Vendors")
        checked_vendor = {}

        checked_vendor["code"] = vendor_code
        checked_vendor["key"] = vendors_store.get(vendor_code, "ERR")
        return checked_vendor
    # -------------------------------------------#
    # Product Setter
    def set_product(self, product_code):
        products_store = Controler.get_data("Products")
        checked_product = {}

        checked_product["code"] = product_code
        checked_product["key"] = products_store.get(product_code, "ERR")
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