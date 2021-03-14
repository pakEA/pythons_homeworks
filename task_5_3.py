from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Кирилл', 'Ян'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def unique_klass():
    klass = []
    for el in klasses:
        if el not in klass:
            klass.append(el)
            yield el


def tutor_gen():
    for tutor, klass in zip_longest(tutors, unique_klass()):
        yield tutor, klass


klass_tutor = tutor_gen()

print(tutor_gen())
for _ in tutor_gen():
    print(next(klass_tutor))

print(next(klass_tutor))
