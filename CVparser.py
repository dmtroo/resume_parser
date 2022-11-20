import os
from UDPipe import parse
import stanza


def check_surname(line):
    if line[5] == 'Animacy=Anim|Case=Nom|Gender=Masc|NameType=Sur|Number=Sing' or line[
        5] == 'Animacy=Anim|Case=Nom|Gender=Fem|NameType=Giv|Number=Sing':
        return True
    return False


def check_name(line):
    if line[5] == 'Animacy=Anim|Case=Nom|Gender=Masc|NameType=Giv|Number=Sing' or line[
        5] == 'Animacy=Anim|Case=Nom|Gender=Fem|NameType=Giv|Number=Sing':
        return True
    return False


def find_fullName(fileName):
    lines = parse(fileName)

    prev_word = ""
    word = ""
    for_check = False

    for line in lines:
        if len(line) > 5:
            if for_check:
                for_check = False
                stanza_check(prev_word + " " + word + " " + line[1])
            elif (check_surname(line) or check_name(line) or line[
                5] == 'Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing' or
                  line[5] == 'Animacy=Anim|Case=Nom|Gender=Fem|Number=Sing'):
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
                print(ent.text)
                break


os.system(
    "curl -F model=ukrainian-iu-ud-2.10-220711 -F data=@input/parse.txt -F tokenizer= -F tagger= -F parser= "
    "https://lindat.mff.cuni.cz/services/udpipe/api/process > output/parse_out.txt")

find_fullName("output/parse_out.txt")
