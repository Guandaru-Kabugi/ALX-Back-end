class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.total = 0
    def add_items(self, item_name, item_price):
        # item_dictionary = {'name': item_name, 'price': price}
        # self.item = item_name
        # self.price = price
        item_dict = {'name': item_name, 'price': item_price}
        # item_dict = {self.item:self.price}
        # self.items.append(item_dict)
        self.items.append(item_dict)
        return self.items
    def stock_price(self):
        # return sum (item['price'] for item in self.items )
        for item in self.items:
            self.total += item['price']
        return self.total
        # for item in self.items:
        #     overall += item['price']
        # return overall
        # for item in self.items:
        #     for price in item.values():
        #         overall += price
        # return overall
#using static and class methods
    @classmethod
    def franchise (cls, store):
        return cls(store.name + " - franchise")
    def __str__(self) -> str:
        return self.name
        # return store.name + " - franchise"
    @staticmethod
    def store_details(store):
        int_value = int(store.stock_price())
        return f"{store.name}, total stock price: {int_value}"


store1 = Store("Walmart")
store1.add_items('Maize',100)
store1.add_items('Rice',200)
store1.add_items('Beans',90)
store1.add_items('Milk',150)
print(store1.items)
price = store1.stock_price()
print(price)
new_shop = Store.franchise(store1)
print(new_shop)
# print (Store.franchise(store1))

print(Store.store_details(store1))