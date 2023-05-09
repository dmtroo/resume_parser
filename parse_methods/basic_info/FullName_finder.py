import json
import stanza


def check_surname(token):
    if token['feats'] == 'Animacy=Anim|Case=Nom|Gender=Masc|NameType=Sur|Number=Sing' or \
            token['feats'] == 'Animacy=Anim|Case=Nom|Gender=Fem|NameType=Giv|Number=Sing':
        return True
    return False


def check_name(token):
    if token['feats'] == 'Animacy=Anim|Case=Nom|Gender=Masc|NameType=Giv|Number=Sing' or \
            token['feats'] == 'Animacy=Anim|Case=Nom|Gender=Fem|NameType=Giv|Number=Sing':
        return True
    return False


def check_in_general(token):
    if token['feats'] == 'Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing' or \
            token['feats'] == 'Animacy=Anim|Case=Nom|Gender=Fem|Number=Sing':
        return True
    return False


def find_fullname(json_data):
    prev_word = ""
    word = ""
    for_check = False

    for sentence in json_data:
        for token in sentence['tokens']:
            if for_check:
                for_check = False
                result = stanza_check(prev_word + " " + word + " " + token['form'])
                if result is not None:
                    return result
            elif check_surname(token) or check_name(token) or check_in_general(token):
                word = token['form']
                for_check = True
            else:
                prev_word = token['form']


def stanza_check(probably_name):
    pipe = stanza.Pipeline("uk", processors="tokenize,ner", package={"iu": ["ncbi_disease", "ontonotes"]},
                           download_method=None, verbose=False, use_gpu=False)
    doc = pipe(probably_name)
    if doc.ents:
        for ent in doc.ents:
            if ent.type == "PERS":
                return ent.text
    return None
