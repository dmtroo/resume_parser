#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# coding=utf-8
import json
import os
from UDPipe import parse
from parse_methods.basic_info import PhoneNum_finder, FullName_finder, Email_finder, SocialNetworkLinks_finder, \
    Gender_finder, Age_finder, Address_finder

# text_file = open("input/parse.txt", encoding='utf-8', mode='r')
# text = text_file.read()

# res = os.system(
#     "curl -F model=ukrainian-iu-ud-2.10-220711 -F data=@input/parse.txt -F tokenizer= -F tagger= -F parser= "
#     "https://lindat.mff.cuni.cz/services/udpipe/api/process > output/parse_out.txt")
# with open('output/parse_out.txt', 'r', encoding='utf-8') as handle:
#     parsed = json.load(handle)
#
#     print(parsed['result'])
# parsed_text = parse("output/parse_out.txt")
#
# full_name = FullName_finder.find_fullName(parsed_text)
# print(full_name)
# PhoneNum_finder.find_number(
#     'asdasd +38 (097) 322 5838 asd +32345 sdflsdfk \n sdp 324 fsdflssd 34 p ksdfs: 0973225838  ssdf')
# Email_finder.find_email('asdasd dmparnak@i.ua asd  sdflsdfk \n sdpfsdflssdp ksdfs: dmytroparnak@ukma.edu.ua ssdf')
# SocialNetworkLinks_finder.find_links(
#     'asdasd https://www.instagram.com/dmytroparnak_/ asd  sdfl https://twitter.com/dmtroo_ sdfk \n sdpfsdflssdp ksdfs: https://www.facebook.com/dmytro.parnak ssdf\nhttps://www.linkedin.com/in/dmparnak/')
# print(Gender_finder.find_gender(parsed_text, text))
# Age_finder.find_age("Дата народження - 8 червня 97")
Address_finder.find_address()
