def tokenize_sentences(parsed_text):
    sentence_texts = []

    for i, line_parts in enumerate(parsed_text):
        if line_parts and len(line_parts) >= 2 and line_parts[1] == 'sent_id':
            if i + 1 < len(parsed_text):
                words_line = parsed_text[i + 1]
                sentence = ' '.join([word_parts for word_parts in words_line[3:]])
                sentence = sentence.replace('\\', '')
                sentence_texts.append(sentence)

    print(f"Number of sentences: {len(sentence_texts)}")
    return sentence_texts
