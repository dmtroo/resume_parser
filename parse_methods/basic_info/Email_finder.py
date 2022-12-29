import re


def find_email(text):
    emails_array = []
    for x in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.-]+", text):
        email = x.group()
        if len(email) > 0:
            emails_array.append(email)

    print(emails_array)
