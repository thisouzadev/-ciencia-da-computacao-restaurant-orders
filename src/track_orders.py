class TrackOrders:

    def __init__(self):
        self.orders = []

    # aqui. deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        count_foods = {}
        for item in self.orders:
            if item[0] == customer:
                if item[1] not in count_foods:
                    count_foods[item[1]] = 1
                else:
                    count_foods[item[1]] += 1

        food_most_frequent = max(count_foods, key=lambda k: count_foods[k])

        return food_most_frequent

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
