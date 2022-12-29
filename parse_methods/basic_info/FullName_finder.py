import stanza


def check_surname(line):
    if line[5] == 'Animacy=Anim|Case=Nom|Gender=Masc|NameType=Sur|Number=Sing' or line[
        5] == 'Animacy=Anim|Case=Nom|Gender=Fem|NameType=Giv|Number=Sing':
        return True
    return False


def check_name(line):
    if line[5] == 'Animacy=Anim|Case=Nom|Gender=Masc|NameType=Giv|Number=Sing' or \
            line[5] == 'Animacy=Anim|Case=Nom|Gender=Fem|NameType=Giv|Number=Sing':
        return True
    return False


def check_in_general(line):
    if line[5] == 'Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing' or \
            line[5] == 'Animacy=Anim|Case=Nom|Gender=Fem|Number=Sing':
        return True
    return False


def find_fullName(text):
    prev_word = ""
    word = ""
    for_check = False

    for line in text:
        if len(line) > 5:
            if for_check:
                for_check = False
                result = stanza_check(prev_word + " " + word + " " + line[1])
                if result is not None:
                    return result
            elif check_surname(line) or check_name(line) or check_in_general(line):
                word = line[1]
                for_check = True
            else:
                prev_word = line[1]


def stanza_check(probably_name):
    pipe = stanza.Pipeline("uk", processors="tokenize,ner", package={"iu": ["ncbi_disease", "ontonotes"]},
                           download_method=None, verbose=False, use_gpu=False)
    doc = pipe(probably_name)
    if doc.ents:
        for ent in doc.ents:
            if ent.type == "PERS":
                return ent.text
    return None

# deeppavlov