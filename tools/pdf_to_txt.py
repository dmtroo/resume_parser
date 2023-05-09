import re
from PyPDF2 import PdfReader

# List of patterns to remove
patterns_to_remove = [
    r"Сайт пошуку роботи №1 в Україні Резюме від \w+ \d{4}",
    r"Отримати контакти цього кандидата можна на сторінці https://www.work.ua/resumes/\d+/",
    r"Сайт пошуку роботи No1 в Україні",
    r"Резюме кандидата розміщено за адресою: www.work.ua/resumes/\d+",
    r"Шукач вказав.*?\."
]


def pdf_to_text(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = " ".join([page.extract_text() for page in reader.pages])

    for pattern in patterns_to_remove:
        text = re.sub(pattern, '', text)

    return text
