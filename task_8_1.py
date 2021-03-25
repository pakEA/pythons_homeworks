import re


def email_parse(email):
    try:
        pattern = re.compile(r'(?P<username>\w+)@(?P<domain>\w+)\.'
                             r'(?P<top_level_domain>\w+)')
        result = pattern.search(email)
        return result.groupdict()
    except AttributeError:
        raise ValueError(f'wrong email: {email}')


email_address = 'someone@geekbrains.ru'
print(email_parse(email_address))
