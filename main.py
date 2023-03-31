from exceptions import RequestError, LogisticError
from request import Request
from shop import Shop
from store import Store


store = Store(
    items={
        'печенька': 25,
        'арахис': 15,
        'сок': 15,
        'арбуз': 55,
    },
)

shop = Shop(
    items={
        'печенька': 1,
        'арахис': 2,
        'сок': 3,
        'арбуз': 5,
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    print('Добрый день!')

    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:{storages[storage_name].get_items()}')

        user_input = input('Введите запрос')
        if user_input in ('stop', 'стоп', 'Стоп', 'Stop'):
            break


        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        try:
            storages[request.departure].remove(request.product, request.amount)
            print('Курьер забрал посылку')
        except LogisticError as error:
            print(error.message)
            continue

        try:
            storages[request.destination].add(request.product, request.amount)
            print('Курьер доставил посылку')
        except LogisticError as error:
            print(error.message)
            storages[request.departure].add(request.product, request.amount)
            print('Курьер вернул посылку')
            continue


if __name__ == '__main__':
    main()

