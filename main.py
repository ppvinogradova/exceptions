documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }

def name_by_number(сatalog):
  number = input('Введите номер документа ')
  name = []
  no_result = 0
  for person in сatalog:
    if number in person.values():
      name.append(person.get('name'))
    else:
      no_result += 1
  if no_result == len(сatalog):
    print('Номер введен неверно или такого документа нет')
  else:
    print(name[0])

def docs_list(сatalog):
  docs_list = []
  for person in сatalog:
    doc_type = person['type']
    doc_num = ' "{}" '.format(person['number'])
    name = '"{}"'.format(person['name'])
    doc_info = doc_type + doc_num + name
    docs_list.append(doc_info)
  print(docs_list)

def shelf_by_number(shelves):
  doc_num = input('Введите номер документа ')
  no_result = 0
  empty_shelves = 0
  for shelf_contents in shelves.values():
    if len(shelf_contents) == 0:
      empty_shelves +=1
    elif doc_num not in shelf_contents:
      no_result += 1
  for shelf_info in shelves.items():
    if doc_num in shelf_info[1]:
      print(shelf_info[0])
  if no_result == len(shelves) - empty_shelves:
    print('Такой документ остустствует')

def add_new_doc(сatalog, shelves):
  doc_num = input('Введите номер документа ')
  doc_type = input('Введите тип документа ')
  name = input ('Введите имя владельца ')
  shelf_num = input('Введите номер полки ')
  new_dict = {"type": doc_type, "number": doc_num, "name": name}
  сatalog.append(new_dict)
  print('Новый документ добавлен в каталог')
  if shelf_num in shelves.keys():
    old_list = shelves.get(shelf_num)
    new_list = old_list.append(doc_num)
    shelves.setdefault(shelf_num, new_list)
  else:
    shelves[shelf_num] = [doc_num]
  print('Новый документ добавлен в перечень полок')
  return сatalog, shelves

def doc_names(catalog):
  try:
    name_list = []
    for doc in catalog:
      name_list.append(doc.get('name'))
    print('Имена владельцев всех документов:')
    for name in name_list:
      print(name)
  except KeyError:
    print('Каталог не содержит имён')

doc_names(documents)

task = input('Введите пользовательскую команду ')
if task == 'p':
  name_by_number(documents)
elif task == 'l':
  docs_list(documents)
elif task == 's':
  shelf_by_number(directories)
elif task == 'a':
  add_new_doc(documents, directories)
else:
  print('Команда введена неверно')