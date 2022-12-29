import re
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering


def find_number(text):
    numbers_array = []
    for x in re.finditer(
            r"(\+\s?[0-9]{0,3}[-/\s.\\]?)?[(]?[0-9]{3}[)]?[-/\s.\\]?[0-9]{2,4}[-/\s.\\]?[0-9]{2,6}[-/\s.\\]?[0-9]{2,6}",
            text):
        number = x.group()
        if len(number) > 6:
            numbers_array.append(format_number(number))

    if not numbers_array:
        answer = answer_question(text, "Номер телефону?")
        numbers_array.append(format_number(answer))

    print(numbers_array)


def format_number(number):
    return re.sub("[^0-9+]", "", number)


def answer_question(text, question):
    model_name = "robinhad/ukrainian-qa"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    qa_model = pipeline("question-answering", model=model.to("cpu"), tokenizer=tokenizer)
    answer = qa_model(question=question, context=text)

    return answer['answer']
