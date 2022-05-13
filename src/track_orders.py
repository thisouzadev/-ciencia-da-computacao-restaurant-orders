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
        menu = []
        customer_eating = []

        for item in self.orders:
            # CRIA UMA LISTA COM O CARDÁPIO
            if item[1] not in menu:
                menu.append(item[1])

            # CRIA UMA LISTA COM TODOS OS PRATOS QUE UM cliente JÁ COMEU
            if item[0] == customer:
                customer_eating.append(item[1])

        set_meu = set(menu)
        set_customer_eating = set(customer_eating)
        return set_meu.difference(set_customer_eating)

    def get_days_never_visited_per_customer(self, customer):
        days = []
        customer_visited = []

        for item in self.orders:
            # CRIA UMA LISTA COM OS DIAS QUE O RESTAURANTE ABRE
            if item[2] not in days:
                days.append(item[2])

            # CRIA UMA LISTA COM OS DIAS QUE O customer FOI AO RESTAURANTE
            if item[0] == customer:
                customer_visited.append(item[2])

        set_days = set(days)
        set_customer_visited = set(customer_visited)
        return set_days.difference(set_customer_visited)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
