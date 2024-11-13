import requests
from lxml import html

# Отправка запроса на сайт
resp = requests.get(url="https://benchmark.best/ru/cpu_table.html", headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0'})

# Построение дерева HTML
tree = html.fromstring(resp.content)

# Извлечение всех строк из таблицы процессоров
proses = tree.xpath("//table[@class='cpus']/tbody/tr")

# Список для хранения информации о процессорах
all_proses = []
for prose in proses:
    id_elements = prose.xpath(".//td[@class='cpus1']/text()")
    name_elements = prose.xpath(".//td[@class='cpus2']/text()")
    frequencyelements = prose.xpath(".//td[@class='cpus4']/text()")

    m = {
        'id': id_elements[0] if id_elements else None,
        'name': name_elements[0] if name_elements else None,
        'frequency': frequencyelements[0] if frequencyelements else None
    }
    all_proses.append(m)

# Печать результата
print(all_proses)
print(len(all_proses))

