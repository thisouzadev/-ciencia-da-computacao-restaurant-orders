import csv


def marias_food_most_frequent(list_data):
    count_foods = {}
    for item in list_data:
        if item["client"] == "maria":
            if item["food"] not in count_foods:
                count_foods[item["food"]] = 1
            else:
                count_foods[item["food"]] += 1

    food_most_frequent = max(count_foods, key=lambda k: count_foods[k])

    return food_most_frequent


def arnaldo_hamburguer_frequency(list_data):
    frequency_foods = {}

    for item in list_data:
        if item["client"] == "arnaldo":
            if item["food"] not in frequency_foods:
                frequency_foods[item["food"]] = 1
            else:
                frequency_foods[item["food"]] += 1

    quantity_burguer = frequency_foods["hamburguer"]

    return str(quantity_burguer)


def joao_never_eat(data):
    menu = []
    joao_eating = []
    for item in data:
        # CRIA UMA LISTA COM O CARDÁPIO
        if item["food"] not in menu:
            menu.append(item["food"])

        # CRIA UMA LISTA COM TODOS OS PRATOS QUE JOÃO JÁ COMEU
        if item["client"] == "joao":
            joao_eating.append(item["food"])

    set_meu = set(menu)
    set_joao_eating = set(joao_eating)
    return set_meu.difference(set_joao_eating)


def joao_days_never_visited(data):
    days = []
    joao_visited = []

    for item in data:
        # CRIA UMA LISTA COM OS DIAS QUE O RESTAURANTE ABRE
        if item["day"] not in days:
            days.append(item["day"])

        # CRIA UMA LISTA COM OS DIAS QUE O JOAO FOI AO RESTAURANTE
        if item["client"] == "joao":
            joao_visited.append(item["day"])

    set_days = set(days)
    set_joao_visited = set(joao_visited)
    return set_days.difference(set_joao_visited)


def analyze_log(path_to_file):
    try:
        with open(path_to_file) as file:
            headers = ["client", "food", "day"]
            data = csv.DictReader(file, fieldnames=headers)
            list_data = [d for d in data]
    except FileNotFoundError:
        if path_to_file[-3:] != 'csv':
            raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open('data/mkt_campaign.txt', 'w') as file:
        file.writelines([
            marias_food_most_frequent(list_data),
            f"\n{arnaldo_hamburguer_frequency(list_data)}",
            f"\n{joao_never_eat(list_data)}"
            f"\n{joao_days_never_visited(list_data)}"
        ])
