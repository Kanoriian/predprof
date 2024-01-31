import csv

with open("students.csv", encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotecher='"')
    data = sorted(reader, key=lambda x: x['tittleProject_id'])

    id_project = None

    while id_project != 'СТОП':
        id_project = int(input("Введите ID проекта >> "))
        for el in data:
            if int(el['tittleProject_id']) == id_project:
                surname, name, patronymic = el["Name"].split()
                print(f"Проект №{id_project} делал: {name[0]}. {surname} он(а) получил(а)")
                break
        else:
            print('Ничего не найдено')
            id_project = int(input("Введите ID проекта >> "))
