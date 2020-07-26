from dataclasses import *


@dataclass
class Product:
    name: str
    price: int
    tax: float


products = [Product("りんご", 150, 1.08), Product("鉛筆", 100, 1.1)]


def sum_price(product):
    return product.price * product.tax


for i in products:
    print(f"商品名: {i.name}\n本体価格: {i.price}\n税込価格: {sum_price(i)}\n")
