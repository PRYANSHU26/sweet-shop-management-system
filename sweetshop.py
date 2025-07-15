class SweetShop:
    def __init__(self):
        self.inventory = []

    def add_sweet(self, sweet_id, name, category, price, quantity):
        sweet = {
            'id': sweet_id,
            'name': name,
            'category': category,
            'price': price,
            'quantity': quantity
        }
        self.inventory.append(sweet)

    def delete_sweet(self, sweet_id):
        self.inventory = [s for s in self.inventory if s['id'] != sweet_id]

    def view_sweets(self):
        return self.inventory

    def search_sweets(self, name=None, category=None, price_min=None, price_max=None):
        results = self.inventory
        if name:
            results = [s for s in results if s['name'].lower() == name.lower()]
        if category:
            results = [s for s in results if s['category'].lower() == category.lower()]
        if price_min is not None and price_max is not None:
            results = [s for s in results if price_min <= s['price'] <= price_max]
        return results

    def sort_sweets(self, by="name", descending=False):
        if by not in ["name", "price"]:
            raise ValueError("Can only sort by 'name' or 'price'")
        return sorted(self.inventory, key=lambda x: x[by], reverse=descending)

    def purchase_sweet(self, sweet_id, quantity):
        for sweet in self.inventory:
            if sweet['id'] == sweet_id:
                if sweet['quantity'] < quantity:
                    raise ValueError("Not enough stock to complete the purchase.")
                sweet['quantity'] -= quantity
                return
        raise ValueError("Sweet not found.")

    def restock_sweet(self, sweet_id, quantity):
        for sweet in self.inventory:
            if sweet['id'] == sweet_id:
                sweet['quantity'] += quantity
                return
        raise ValueError("Sweet not found.")
