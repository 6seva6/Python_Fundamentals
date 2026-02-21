class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.filtered_list = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        for i in self.products:
            if i.startswith(letter):
                self.filtered_list.append(i)
        return self.filtered_list

    def __repr__(self):
        return f"Items in the {self.name} catalogue:\n" + "\n".join(sorted(self.products))

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)