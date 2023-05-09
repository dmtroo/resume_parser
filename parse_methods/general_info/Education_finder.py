import pandas as pd
from deeppavlov import build_model
df = pd.read_excel('additional_info/universities.xlsx')


def find_date(tags, tokens):
    date_enter_graduate = []
    for idx, tag in enumerate(tags[0]):
        if tag == 'B-DATE' or tag == 'I-DATE':
            date_enter_graduate.append(tokens[0][idx])
    return date_enter_graduate


def find_university(parsed_json):
    education = []
    university = ''
    ner_model = build_model('ner_ontonotes_bert_mult', download=False, install=False)

    for sentence in parsed_json:
        sent = sentence['text']
        tokens, tags = ner_model([sent])

        for idx, tag in enumerate(tags[0]):
            if tag == 'B-ORG':
                university += tokens[0][idx]
                for idx2 in range(idx + 1, len(tags[0])):
                    if tags[0][idx2] == 'I-ORG':
                        tok = tokens[0][idx2]
                        if tok == 'ім':
                            tok = 'імені'
                        if tok == '.' or tok == '"' or tok == '-':
                            continue
                        else:
                            university += f" {tok}"

                if university:
                    result = extract_university(university)
                    university = ''
                    if result != (None, None, None, None):
                        education_info = {
                            "university": result[0],
                            "abbreviation": result[1],
                            "university_english": result[2],
                            "webpage": result[3],
                            "date_range": find_date(tags, tokens)
                        }
                        education.append(education_info)
    if not education:
        result = extract_university(parsed_json[0]['text'])
        if result != (None, None, None, None):
            education_info = {
                "university": result[0],
                "abbreviation": result[1],
                "university_english": result[2],
                "webpage": result[3],
                "date_range": None
            }
            education.append(education_info)
    return education


def extract_university(cv_text):
    for index, row in df.iterrows():
        first4words = row['Назва закладу освіти'].split()[:4]
        first4words_uni = ' '.join(map(str, first4words)).replace('"', '').replace('-', ' ')
        abbreviation = str(row['Коротка назва'])
        if first4words_uni in cv_text or (abbreviation in cv_text and abbreviation != '.'):
            return (row['Назва закладу освіти'] if pd.notnull(row['Назва закладу освіти']) else None,
                    abbreviation if pd.notnull(abbreviation) else None,
                    row['Назва закладу освіти (англ.)'] if pd.notnull(row['Назва закладу освіти (англ.)']) else None,
                    row['Веб-сайт'] if pd.notnull(row['Веб-сайт']) else None)
    return None, None, None, None
