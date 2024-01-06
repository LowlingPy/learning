# mahdi mohammadi khah 982011056

import re


def date_format_changer(date_str):
    match = re.findall(r'(\d{4})-(\d{2})-(\d{2})', date_str)
    if match:
        year, month, day = match[0]
        return f'{day}-{month}-{year}'
    else:
        return 'Try again please'


original_date = input()
converted_date = date_format_changer(original_date)
print(f'New date in DD-MM-YYYY Format: {converted_date}')
print(converted_date)
