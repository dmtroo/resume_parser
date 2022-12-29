import re


def find_gender(parsed_text, text):
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
        return udPipe_check(parsed_text)


def udPipe_check(parsed_text):
    for line in parsed_text:
        if len(line) > 5:
            if line[5] == 'Animacy=Anim|Case=Nom|Gender=Masc|NameType=Giv|Number=Sing':
                return "male"
            elif line[5] == 'Animacy=Anim|Case=Nom|Gender=Fem|NameType=Giv|Number=Sing':
                return "female"
    return None

# додати на -а -я жіночі імена