import csv


class TrackOrders:
    orders = []
    days = set()
    order = set()

    def __init__(self):
        self.orders = []
        self.days = set()
        self.order = set()

        with open("data/orders_1.csv") as orders_file:
            reader = csv.DictReader(
                orders_file, fieldnames=["customer", "meal", "day"]
            )

            for order in reader:
                self.days.add(order["day"])
                self.order.add(order["meal"])

    # aqui. deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({"customer": customer, "meal": order, "day": day})

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
