import json
import hashlib


# Задание №1
class CountryIterator:
    def __init__(self, countries_list):
        self.countries_list = countries_list
        self.item_index = 0
        self.wiki_url = 'https://en.wikipedia.org/wiki/'

    def __iter__(self):
        return self

    def __next__(self):
        if self.item_index == len(self.countries_list):
            raise StopIteration
        current_item = self.countries_list[self.item_index]
        self.item_index += 1

        return current_item, self.wiki_url + f'{current_item}'


countries_list = []
with open('countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        countries_list.append(item['name']['common'].replace(' ', '_'))

countries_dict = {}
for country in CountryIterator(countries_list):
    countries_dict.setdefault(country[0], country[1])

with open('country_url.json', 'w', encoding='utf-8') as f:
    json.dump(countries_dict, f, ensure_ascii=False, indent=2)


# Задание №2
def my_hash(file_path):
    file_name = file_path.split('/')[0]
    with open(f'{file_name}', 'r', encoding='utf-8') as f:
        for line in f:
            hash_line = hashlib.md5(line.encode())
            yield hash_line.hexdigest()


for item in my_hash('test.txt'):
    print(item)
