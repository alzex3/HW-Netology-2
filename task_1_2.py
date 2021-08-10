from pprint import pprint

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        count = int(file.readline().strip())
        ingredients = []
        recipe = []
        for i in range(count):
            ingredients.append(file.readline().strip().split(' | '))
        for name, qt, measure in ingredients:
            recipe.append({'ingredient_name': name, 'quantity': int(qt), 'measure': measure})
        cook_book[dish.strip()] = recipe
        file.readline().strip()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = \
                        {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count

        else:
            print(f'Блюда "{dish}" нет в книге рецептов!')
    pprint(shop_list)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1)
