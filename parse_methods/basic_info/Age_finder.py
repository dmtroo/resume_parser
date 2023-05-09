import re
from deeppavlov import build_model
from dateutil.parser import parse


def find_age(text):
    lines = text.splitlines()

    for i, line in enumerate(lines):
        if re.search(r"(Дата народження|дата народження|Народився|народився)", line):
            match = re.search(
                r"(\d{1,2}[-/.\s]\d{1,2}[-/.\s]'?\d{2,4})|(\d{2,4}[-/.\s]\d{1,2}[-/\s]\d{1,2})|(\d{1,2}\s*(?:rd|th|st)?\s*(січня|лютого|березня|квітня|травня|червня|липня|серпня|вересня|жовтня|листопада|грудня)\s*?[-/,]?\s*'?\d{2,4})",
                line)
            if match:
                return is_date(match.group(0))
            else:
                match = re.search(
                    r"(\d{1,2}[-/.\s]\d{1,2}[-/.\s]'?\d{2,4})|(\d{2,4}[-/.\s]\d{1,2}[-/\s]\d{1,2})|(\d{1,2}\s*(?:rd|th|st)?\s*(січня|лютого|березня|квітня|травня|червня|липня|серпня|вересня|жовтня|листопада|грудня)\s*?[-/,]?\s*'?\d{2,4})",
                    lines[i + 1])
                return is_date(match.group(0))


def is_date(date):
    ner_model = build_model('ner_ontonotes_bert_mult', download=False, install=False)
    tokens, tags = ner_model([date])
    for idx, tag in enumerate(tags[0]):
        if tag == 'B-DATE' or tag == 'I-DATE':
            return parse(date, fuzzy=True)
