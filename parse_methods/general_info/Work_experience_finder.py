import re
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering


def find_work_experience(json_result):
    work_experience = []

    found_work_experience = False
    job_title_ok = False
    company_ok = False
    date_range_ok = False

    for i, sentence in enumerate(json_result):
        if not found_work_experience:
            if any(lemma in ('досвід', 'робота') for token in sentence['tokens'] for lemma in (token['lemma'],)):
                found_work_experience = True

        if found_work_experience:
            if any(lemma in ('освіта', 'навчання', 'курс', 'сертифікат') for token in sentence['tokens'] for lemma in (token['lemma'],)):
                break
            text = sentence['text']

            if not job_title_ok:
                job_title = answer_question(text, 'яка посада?')

            if not company_ok:
                company = answer_question(text, 'яка компанія?')

            if not date_range_ok:
                date_range = answer_question(text, 'період часу?')

            company_check = None
            for token in sentence['tokens']:
                if token['xpos'] == 'Npmsnn' or token['xpos'] == 'Npmsny' or token['xpos'] == 'Y':
                    company_check = token['form']
                    break

            if not company_ok:
                company_ok = company_check is not None and company_check in company
            if not date_range_ok:
                date_range_ok = bool(re.search(r'\d', date_range))
            if not job_title_ok:
                job_title_ok = bool(job_title) and bool(re.search(r'[a-zA-Zа-яА-Я]', job_title))

            # Append the information to work_experience if all conditions are met
            if company_ok and date_range_ok and job_title_ok:
                work_experience.append({
                    'job_title': job_title,
                    'company': company,
                    'date_range': date_range
                })

                job_title_ok = False
                company_ok = False
                date_range_ok = False

    return work_experience


def answer_question(text, question):
    model_name = "robinhad/ukrainian-qa"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    qa_model = pipeline("question-answering", model=model.to("cpu"), tokenizer=tokenizer)
    answer = qa_model(question=question, context=text)

    return answer['answer']
