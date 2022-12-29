import re
from dateutil.parser import parse
import datetime as dt


def find_age(text):
    for line in text.splitlines():
        if re.search(r"(Дата народження|дата народження|Народився|народився)", line):
            match = re.search(r"(\d{1,2}[-/.\s]\d{1,2}[-/.\s]'?\d{2,4})|(\d{2,4}[-/.\s]\d{1,2}[-/\s]\d{1,2})|(\d{1,2}\s*(?:rd|th|st)?\s*(січня|лютого|березня|квітня|травня|червня|липня|серпня|вересня|жовтня|листопада|грудня)\s*?[-/,]?\s*'?\d{2,4})", line)
            is_date(match.group(0))

def is_date(date):
    print(parse(date, fuzzy=True))
    # fmts = (
    #     '%Y', '%b %d, %Y', '%d %b %Y', '%B %d, %Y', '%B %d %Y', '%d/%m/%Y', '%d/%m/%y', '%m/%d/%Y', '%m/%d/%y', '%b %Y', '%B%Y', '%b %d,%Y')
    #
    # parsed = []
    # for fmt in fmts:
    #     try:
    #         t = dt.datetime.strptime(date, fmt)
    #         parsed.append((date, fmt, t))
    #         break
    #     except ValueError:
    #         pass
    #
    # for t in parsed:
    #     print('"{:20}" => "{:20}" => {}'.format(*t))
