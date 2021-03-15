def thesaurus(*elem):
    list_of_names = list(map(str, elem))
    names = []

    for name in list_of_names:
        dict_of_names.setdefault(f'{name[0].title()}', name)
        key = name[0].title()

        for person_name in list_of_names:
            if person_name.startswith(key.title()) or \
                    person_name.startswith(key.lower()):
                names.append(person_name.title())
        dict_of_names[key] = names
        names = []

    print(dict_of_names)


dict_of_names = {}

thesaurus('Иван', 'Максим', 'Артём', 'ирина', 'Адам', 'Илья')
