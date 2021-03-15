class VatService:

    def __init__(self, vat_value=0.23):
        self.vat_value = vat_value

    def get_gross_price_for_default_vat(self, product):
        return self.get_gross_price(product.net_price, product.vat_price)

    def get_gross_price(self, net_price, vat_value):
        if vat_value > 1:
            raise ValueError('VAT value should be less than 1')
        return net_price * (1 + vat_value)


class Product:
    def __init__(self, id, net_price):
        self.id = id
        self.net_price = net_price


def main():
    product1 = Product(1, 100)
    print(VatService.get_gross_price_for_default_vat(product1))


main()
