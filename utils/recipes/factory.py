from random import randint
from faker import Faker
from pprint import pprint

def rand_ratio():
    # Retorna dois valores aleatórios. To usando mais especificamento para o 'cover' do make_recipe()
    return randint(840, 900), randint(473, 573)

fake = Faker('pt-br')

def get_image_url_only():
    width, height = rand_ratio()
    bluid_url = f'https://picsum.photos/{width}/{height}'
    return bluid_url

def make_recipe():
    # Gera dados fakes
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porções',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name()
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': get_image_url_only()
        }
    }

# Informa que esse é um módulo python. pprint descobri recentemente... Ele só imprime de forma mais bonita
if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())