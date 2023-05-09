import json


def conllu_to_json(conllu):
    sentences = []
    current_sentence = {}
    current_tokens = []

    for line in conllu.split('\n'):
        if line.startswith('#'):
            if line.startswith('# sent_id'):
                if current_sentence:
                    current_sentence['tokens'] = current_tokens
                    sentences.append(current_sentence)
                current_sentence = {'sent_id': line.split('=')[-1].strip()}
                current_tokens = []
            elif line.startswith('# text'):
                current_sentence['text'] = line.split('=')[-1].strip()
        elif line.strip():
            columns = line.split('\t')
            token = {'id': columns[0],
                     'form': columns[1],
                     'lemma': columns[2],
                     'upos': columns[3],
                     'xpos': columns[4],
                     'feats': columns[5],
                     'head': columns[6],
                     'deprel': columns[7],
                     'deps': columns[8],
                     'misc': columns[9]}
            current_tokens.append(token)

    if current_sentence:
        current_sentence['tokens'] = current_tokens
        sentences.append(current_sentence)

    return sentences


def save_json_to_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
