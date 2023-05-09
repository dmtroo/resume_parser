import json
import os
from UDPipe import parse
from parse_methods.basic_info import PhoneNum_finder, FullName_finder, Email_finder, SocialNetworkLinks_finder, \
    Gender_finder, Age_finder, Address_finder
from parse_methods.general_info import Education_finder, Work_experience_finder, Salary_finder
from tools.conllu_to_json import conllu_to_json, save_json_to_file
from tools.pdf_to_txt import pdf_to_text
from transformers import logging

logging.set_verbosity_error()

RESUME_FOLDER = "/Users/dmtroo/Documents/Study/NaUKMA/Coursework/test_database"
OUTPUT_FILE = "output/output.json"

output_list = []

for filename in os.listdir(RESUME_FOLDER):
    print(filename)
    if filename.endswith(".pdf"):
        path_to_file = os.path.join(RESUME_FOLDER, filename)

        text = pdf_to_text(path_to_file)
        with open('input/parse.txt', 'w', encoding='utf-8') as f:
            f.write(text)

        res = os.system(
            "curl -F model=ukrainian-iu-ud-2.10-220711 -F data=@input/parse.txt -F tokenizer= -F tagger= -F parser= "
            "https://lindat.mff.cuni.cz/services/udpipe/api/process > output/parse_out.txt")

        with open('output/parse_out.txt', 'r', encoding='utf-8') as handle:
            parsed = json.load(handle)

        parsed_text = parse("output/parse_out.txt")

        conllu_result = parsed['result']
        json_result = conllu_to_json(conllu_result)
        save_json_to_file(json_result, 'output/parse_out.json')

        text_file = open("input/parse.txt", encoding='utf-8', mode='r')
        text = text_file.read()

        full_name = FullName_finder.find_fullname(json_result)
        age = Age_finder.find_age(text)
        number = PhoneNum_finder.find_number(text)
        email = Email_finder.find_email(text)
        networks = SocialNetworkLinks_finder.find_links(text)
        gender = Gender_finder.find_gender(json_result, text, full_name)
        salary = Salary_finder.find_salary(text)
        address = Address_finder.find_address(json_result)
        university = Education_finder.find_university(json_result)
        work_experience = Work_experience_finder.find_work_experience(json_result)

        output_dict = {
            "filename": filename,
            "full_name": full_name,
            "age": age,
            "phone_number": number,
            "email": email,
            "social_network_links": networks,
            "gender": gender,
            "salary": salary,
            "address": address,
            "education": university,
            "work_experience": work_experience
        }

        output_list.append(output_dict)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(output_list, f, ensure_ascii=False, indent=4)
