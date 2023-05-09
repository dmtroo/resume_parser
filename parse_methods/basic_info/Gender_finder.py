import re


def find_gender(parsed_json, text, full_name):
    match = re.search(r"((Стать|стать)[:\-\s]*\w+)", text)
    if match:
        gender = match.group(1).split()[-1].lower()
        if gender == 'чоловік' or gender == 'чоловіча':
            return 'male'
        elif gender == 'жінка' or gender == 'жіноча':
            return 'female'
        else:
            return 'differentRepresentation'
    else:
        return udPipe_check(parsed_json, full_name)


def udPipe_check(parsed_json, name):
    for sentence in parsed_json:
        for token in sentence['tokens']:
            if token['feats'] == 'Animacy=Anim|Case=Nom|Gender=Masc|NameType=Giv|Number=Sing':
                return "male"
            elif token['feats'] == 'Animacy=Anim|Case=Nom|Gender=Fem|NameType=Giv|Number=Sing':
                return check_female(name)
    return None


def check_female(name):
    if name:
        if name.endswith(('а', 'я', 'в')):
            return "female"
